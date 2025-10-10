import os
from flask import Blueprint, redirect, url_for, render_template, g, request, current_app, send_from_directory
from werkzeug.utils import secure_filename

from main import db
# User 모델을 임포트해야 함
from main.models import User, Product
from main.forms import UserCreateForm

bp = Blueprint('member', __name__, url_prefix='/member')

# # mypage 전용 정적 라우트 (팩토리 구조 대응)
# @bp.route('/mypage_js/<path:filename>')
# def mypage_static(filename):
#     """
#     /member/mypage_js/ 요청 시 main/static/mypage_js에서 파일을 반환
#     """
#     # root_path는 이미 main을 가리키므로 'main'을 추가하면 안 됨
#     static_dir = os.path.join(current_app.root_path, 'static', 'mypage_js')
#     return send_from_directory(static_dir, filename)


@bp.route('/mypage', methods=['GET', 'POST'])
def mypage():
    form = UserCreateForm()
    product_list = Product.query.order_by(Product.create_date)
    page = request.args.get('page', default=1, type=int) # 페이지


    if request.method == 'POST':
        formimage = form.image.data
        image = 'user_img/default.jpg'
        if formimage:
            upload_folder = os.path.join(current_app.root_path, 'static/user_img', str(g.user.id))

            os.makedirs(upload_folder, exist_ok=True)

            filename = secure_filename(formimage.filename)
            file_path = os.path.join(upload_folder, filename)
            formimage.save(file_path)


            g.user.image = f'user_img/{g.user.id}/{filename}'
            db.session.commit()
        return redirect(url_for('member.mypage',))

    product_list = product_list.paginate(page=page, per_page=10)  # 한페이지에 보여야할 게시물



    return render_template('member/mypage.html', user=g.user, form=form, page=page, product_list=product_list)

@bp.route('/create', methods=['GET'])
def create():
    return render_template('items/items_form.html')