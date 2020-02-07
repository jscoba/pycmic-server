import functools, os

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app, abort,
    jsonify
)

from pycmicserver.db import get_db

from pycmicserver.utils import autenticacion, incrementa_valor, user_in_db

from pycmicserver.csv_parser import Csv_parser

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
        db.commit()
        incrementa_valor(auth[0].lower()+'_access', db)
        return jsonify(dict(u))


""" get_users - Devuelve todos los usuarios disponibles

Parámetros: 
 - authkey como a por GET

 Comprueba que el usuario está autorizado (es administrador), si lo está devuelve los detalles de
 todos los usuarios de la base de datos
 """

@bp.route('/get_users', methods=['GET'])
def get_users():
    auth = autenticacion(request, current_app)
    if 'ADMIN' not in auth:
        current_app.logger.info("Usuario sin autorización ha intentado hacer una petición")
        abort(403)
    db = get_db()
    u = db.execute('SELECT * FROM usuarios').fetchall()

    return jsonify([dict(i) for i in u])


""" force_update - Fuerza la actualización de la base de datos desde un CSV dado

Parámetros: 
 - authkey como a por GET

 Comprueba que el usuario está autorizado (es administrador), si lo está parsea el fichero CSV
 de la impresora y actualiza la información de los usuarios en la base de datos.
 """

@bp.route('/force_update', methods=['GET'])
def force_update():
    auth = autenticacion(request, current_app)
    if 'ADMIN' not in auth:
        current_app.logger.info("Usuario sin autorización ha intentado hacer una petición")
        abort(403)
    db = get_db()
    c = Csv_parser(os.path.join(os.path.dirname(__file__),'example.csv'))
    users = c.return_users()
    nuevos = 0
    actualizados = 0
    for u in users:
        if user_in_db(u['usercode'],db):
            db.execute("UPDATE usuarios SET nombre = ?, copias_max = ?, copias_used = ? WHERE usercode = ?", (u['name'], u['copias_max'], u['copias_used'], u['usercode'],))
            actualizados +=1
        else:
            db.execute("INSERT INTO usuarios (nombre, usercode, copias_max, copias_used, last_login) VALUES (?, ? , ?, ?, DATE('now'));", (u['name'], u['usercode'], u['copias_max'], u['copias_used'],))
            nuevos+=1
    db.execute("UPDATE stats SET valor = DATE('now') WHERE clave = 'last_check'")
    db.commit()
    current_app.logger.info('Nuevo CSV cargado en la base de datos')
    current_app.logger.info('Nuevos: '+str(nuevos)+' Actualizados: '+str(actualizados))
    return jsonify({'status':'ok', 'nuevos':nuevos, 'actualizados':actualizados})


"""link_user - Asocia un usuario a un DNI

Parámetros: 
 - usercode:int por url
 - dni:str por url
 - authkey como a por GET

 Comprueba que el usuario está autorizado, si lo está enlaza el dni dado con
 el usuario o un error 404 si este no existe
""" 

@bp.route('/link_user/<int:usercode>/<string:dni>', methods=['GET'])
def link_user(usercode, dni):
    auth = autenticacion(request, current_app)
    if len(auth) == 0:
        current_app.logger.info("Usuario sin autorización ha intentado hacer una petición")
        abort(403)
    db = get_db()
    u = db.execute('SELECT * FROM usuarios WHERE usercode = ?', (usercode,)).fetchone()
    if u is None:
        abort(404)
    else:
        db.execute("UPDATE usuarios SET dni = ? WHERE usercode = ?", (dni, usercode,))
        db.commit()
        incrementa_valor(auth[0].lower()+'_access', db)
        return jsonify({'status':'OK'})


"""get_pasos - Devuelve un usuario a partir de DNI si existe o 404

Parámetros: 
 - dni:str por url
 - authkey como a por GET

 Comprueba que el usuario está autorizado, si lo está devuelve los detalles del
 usuario de la base de datos o un error 404 si este no existe
""" 

@bp.route('/get_pasos/<string:dni>', methods=['GET'])
def get_pasos(dni):
    auth = autenticacion(request, current_app)
    if len(auth) == 0:
        current_app.logger.info("Usuario sin autorización ha intentado hacer una petición")
        abort(403)
    db = get_db()
    u = db.execute('SELECT * FROM usuarios WHERE dni = ?', (dni,)).fetchone()
    if u is None:
        abort(404)
    else:
        db.execute("UPDATE usuarios SET last_login = DATE('now') WHERE usercode = ?", (u['usercode'],))
        db.commit()
        incrementa_valor(auth[0].lower()+'_access', db)
        return jsonify(dict(u))
