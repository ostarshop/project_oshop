import os
from flask import Blueprint, redirect, url_for, render_template, g, request, current_app
from werkzeug.utils import secure_filename

from main import db
# User 모델을 임포트해야 함
from main.models import User
from main.forms import UserCreateForm

bp = Blueprint('member', __name__, url_prefix='/member')

@bp.route('/mypage', methods=['GET', 'POST'])
def mypage():
    form = UserCreateForm()
    if request.method == 'POST':
        form_image = form.image.data
        image = 'user_img/default.jpg'
        if form_image:
            upload_folder = os.path.join(current_app.root_path, 'static/user_img', str(g.user.id))

            os.makedirs(upload_folder, exist_ok=True)

            filename = secure_filename(form_image.filename)
            file_path = os.path.join(upload_folder, filename)
            form_image.save(file_path)


            g.user.image = f'user_img/{g.user.id}/{filename}'
            db.session.commit()

        return redirect(url_for('member.mypage',))


    return render_template('member/mypage.html', user=g.user, form=form)

@bp.route('/create', methods=['GET'])
def create():
    return render_template('items/items_form.html')