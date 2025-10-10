from datetime import datetime
from itertools import product

from flask import Blueprint, render_template, request, flash, url_for, redirect, g
from main import db
from main.models import Product
from main.forms import ProductForm
from main.views.auth_views import login_required

bp = Blueprint('items', __name__, url_prefix='/items')

@bp.route('/main/')
def _main():
    return render_template('items/items_main.html')

@bp.route('/list/')
def _list():
    products = Product.query.all()
    return render_template('items/items_list.html', products=products)

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        #  html 입력한 값 받아오기
        title = request.form['title']
        price = int(request.form.get('price') or 0)
        color = request.form.get('color')
        content = request.form.get('description', '내용없음')

        # 이미지 업로드
        file = request.files.get('image_url')   # keyError 방지
        img_path = None
        if file and file.filename != '':
            save_path = f"main/static/uploads/{file.filename}"
            file.save(save_path)
            img_path = f"/static/uploads/{file.filename}"

        #  DB 저장하기
        product = Product(
            title=title,
            content=content,    # content 필수 채움
            price=price,
            img_path=img_path,
            color=color,
            create_date=datetime.now(),
            user_id=getattr(g.user, 'id', 1)    # 로그인 없으면 임시 1번 유저로
        )
        try:
            db.session.add(product)
            db.session.commit()
            # 저장 완료 후, 상품 목록 페이지로 이동
            flash('상품이 성공적으로 등록되었습니다!', 'success')
            return redirect(url_for('items._list'))
        except Exception as e:
            db.session.rollback()
            flash(f'상품 등록 중 오류 발생: {e}', 'danger')
    # 처음 들어왔을떈 GET요청 / 끝 화면 보여주기
    return render_template('items/items_form.html')

@bp.route('/')
def list():
    products = Product.query.all()
    return render_template('items/items_list.html', products=products)