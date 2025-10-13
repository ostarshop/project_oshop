from datetime import datetime
from flask import Blueprint, render_template, request, flash, url_for, redirect, g, current_app
from werkzeug.utils import secure_filename
import os
from main import db
from main.models import Product, ProductImage
from main.views.auth_views import login_required

bp = Blueprint('items', __name__, url_prefix='/items')


@bp.route('/main/')
def _main():
    event = Product.query.filter_by(tags='이벤트').all()
    clothing = Product.query.filter_by(tags='의류').all()
    accessory = Product.query.filter_by(tags='악세서리').all()
    misc = Product.query.filter_by(tags='잡화').all()


    return render_template('items/items_main.html',event=event, clothing=clothing, misc=misc, accessory=accessory)


@bp.route('/list/')
def _list():
    products = Product.query.order_by(Product.create_date.desc()).all()
    return render_template('items/items_list.html', products=products)


@bp.route('/create', methods=['GET', 'POST'])
@login_required # 로그인한 사용자만 접근이 가능
def create():
    if request.method == 'POST':
        #  html 입력한 값 받아오기
        title = request.form['title']
        price = int(request.form.get('price') or 0)
        discount = request.form.get('discount')
        tags = request.form.get('tags')
        content = request.form.get('description', '내용없음')
        user_id = g.user.id

        #  DB 저장하기
        product = Product(
            title=title,
            content=content,  # content 필수 채움
            price=price,
            discount=discount,
            create_date=datetime.now(),
            tags = tags,
            user_id=user_id
        )
        db.session.add(product)
        db.session.commit()     # db 에 먼저 저장해서 product.id 확보

        files = request.files.getlist('images') # 여러 이미지 가져오기
        upload_folder = os.path.join(current_app.root_path, 'static/product_img', str(g.user.id)) # 저장할 경로
        os.makedirs(upload_folder, exist_ok=True) # 경로에 해당하는 파일이 없으면 생성

        for file in files:
            if file and file.filename != '': # 파일 존재 확인
                filename = file.filename # 안전한 파일명
                filepath = os.path.join(upload_folder, filename) # 저장 경로
                file.save(filepath) # 서버에 파일 저장

                product_image = ProductImage(
                    product_id=product.id,
                    img_path=f'product_img/{g.user.id}/{filename}' # 저장하면서 경로에 userid추가
                )
                db.session.add(product_image)

        db.session.commit()
        flash('상품 등록 완료!', 'success')
        return redirect(url_for('items._list'))

    return render_template('items/items_form.html')


@bp.route('/detail/<int:product_id>')
def detail(product_id):
    products = Product.query.order_by(Product.create_date.desc()).all()
    product = Product.query.get_or_404(product_id)
    return render_template('items/items_detail.html', product=product, products=products )


@bp.route('/delete/<int:product_id>')
@login_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)

    # 작성자이거나 관리자이면 삭제 가능
    if g.user.id != product.user_id and not g.user.admin:
        flash('삭제 권한이 없습니다.', 'danger')
        return redirect(url_for('items._list'))

    # 상품 이미지 먼저 삭제
    ProductImage.query.filter_by(product_id=product.id).delete()

    # 상품 삭제
    db.session.delete(product)
    db.session.commit()
    flash('상품이 삭제되었습니다.', 'success')

    return redirect(url_for('member.mypage'))


