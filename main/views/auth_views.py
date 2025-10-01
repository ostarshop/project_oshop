import functools

from flask import Blueprint, redirect, url_for, request, flash, render_template, session,g
from werkzeug.security import generate_password_hash, check_password_hash

from main import db
from main.models import User
from main.forms import UserCreateForm, UserLoginForm

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            user = User(userid=form.userid.data,
                        username=form.username.data,
                        password=generate_password_hash(form.password1.data),
                        email=form.email.data,
                        phone=form.phone.data,
                        address=form.address.data                 
                        )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('auth/signup.html', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(userid=form.userid.data).first()
        if not user:
            error = '존재하지 않는 사용자입니다.'
        elif not check_password_hash(user.password, form.password.data):
            error = '비밀번호가 올바르지 않습니다.'
        if error is None:
            session.clear()
            session['user_id'] = user.id
            _next = request.args.get('next', '')
            if _next:
                return redirect(_next)
            else:
                return redirect(url_for('main.index'))
        flash(error)
    return render_template('auth/login.html', form=form) # GET 방식으로 로그인 요청시 html 문서가 나오도록

# 로그인한 사용자면 g.user에 유저 정보를 받아서 저장
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(int(user_id))

# 로그아웃시 session을 삭제하고 메인 으로 보냄
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.index'))

# 특정 페이지에 로그인한 유저가 아니면 로그인페이지로 보냄
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(*args ,**kwargs):
        if g.user is None:
            _next = request.url if request.method == 'GET' else ''
            return redirect(url_for('auth.login', next=_next))
        return view(*args, **kwargs)
    return wrapped_view