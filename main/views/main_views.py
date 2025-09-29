# url 설정
from flask import Blueprint, redirect, url_for, render_template

# 블루 프린트 설정
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return redirect(url_for('items._main'))  # 템플릿을 직접 렌더링
