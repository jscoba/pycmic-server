# Funciones auxiliares a las vistas para hacerles el trabajo más fácil

"""Devuelve una lista con los usuarios autorizados de una petición o una lista vacía"""

def autenticacion(request, app):
    r = []
    if request.args.get('a') == app.config['ADMIN_KEY']:
        r.append('ADMIN')
    if request.args.get('a') == app.config['CLIENT_KEY']:
        r.append('CLIENT')
    if request.args.get('a') == app.config['WEB_KEY']:
        r.append('WEB')
    return r

def incrementa_valor(clave, db):
    db.execute("UPDATE stats SET valor = valor + 1 WHERE clave = ?", (clave,))
    db.commit()


def user_in_db(usercode, db):
    r = db.execute("SELECT usercode FROM usuarios WHERE usercode = ?", (usercode,)).fetchone()
    return r is not None 