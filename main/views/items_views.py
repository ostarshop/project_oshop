
from flask import Blueprint, redirect, url_for, render_template

bp = Blueprint('items', __name__, url_prefix='/items')

@bp.route('/main/')
def _main():
    return render_template('items/items_main.html')

@bp.route('/list/')
def _list():
    return render_template('items/items_list.html')