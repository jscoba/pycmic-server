import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)
from werkzeug.security import check_password_hash, generate_password_hash

from pycmicserver.db import get_db

bp = Blueprint('pycmicserver', __name__)

@bp.route('/test', methods=['GET'])
def test_view():
    print(current_app.config)
    return 'Prueba correcta'