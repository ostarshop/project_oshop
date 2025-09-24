# url 설정
from flask import Blueprint

# 블루 프린트 설정
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return '시작이다~'
