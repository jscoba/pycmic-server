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