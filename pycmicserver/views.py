import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app, abort,
    jsonify
)

from pycmicserver.db import get_db

from pycmicserver.utils import autenticacion

bp = Blueprint('pycmicserver', __name__)

@bp.route('/test', methods=['GET'])
def test_view():
    print(current_app.config)
    return 'Prueba correcta'


"""get user - Devuelve un usuario si existe o 404

Parámetros: 
 - usercode:int por url
 - authkey como a por GET

 Comprueba que el usuario está autorizado, si lo está devuelve los detalles del
 usuario de la base de datos o un error 404 si este no existe
""" 

@bp.route('/get_user/<int:usercode>', methods=['GET'])
def get_user(usercode):
    auth = autenticacion(request, current_app)
    if len(auth) == 0:
        current_app.logger.info("Usuario sin autorización ha intentado hacer una petición")
        abort(403)
    db = get_db()
    u = db.execute('SELECT * FROM usuarios WHERE usercode = ?', (usercode,)).fetchone()
    if u is None:
        abort(404)
    else:
        db.execute("UPDATE usuarios SET last_login = DATE('now') WHERE usercode = ?", (usercode,))
        db.execute("UPDATE stats SET valor = valor + 1 WHERE clave = ?", (auth[0].lower()+'_access',))
        db.commit()
        return jsonify(dict(u))


""" get_users - Devuelve todos los usuarios disponibles

Parámetros: 
 - usercode:int por url
 - authkey como a por GET

 Comprueba que el usuario está autorizado, si lo está devuelve los detalles del
 usuario de la base de datos o un error 404 si este no existe
 """

@bp.route('/get_users', methods=['GET'])
def get_users():
    pass

# force_update

# link_user

# get_pasos