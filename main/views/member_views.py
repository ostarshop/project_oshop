import os
from flask import Blueprint, redirect, url_for, render_template, g, request, current_app
from werkzeug.utils import secure_filename

from main import db
# User 모델을 임포트해야 함
from main.models import User, Product
from main.forms import UserCreateForm

bp = Blueprint('member', __name__, url_prefix='/member')


@bp.route('/mypage', methods=['GET', 'POST'])
def mypage():
    form = UserCreateForm()
    page = request.args.get('page', default=1, type=int)  # 페이지
    if g.user.admin:
        product_list = Product.query.order_by(Product.create_date.desc()) \
            .paginate(page=page, per_page=7)
    else:
        product_list = Product.query \
            .filter_by(user_id=g.user.id) \
            .order_by(Product.create_date.desc()) \
            .paginate(page=page, per_page=7)

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
        return redirect(url_for('member.mypage'))

    return render_template('member/mypage.html', user=g.user, form=form, page=page, product_list=product_list)


@bp.route('/create', methods=['GET'])
def create():
    return render_template('items/items_form.html')
