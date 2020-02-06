
from flask import Flask, jsonify
import os


def create_app(test_config=None):
    # crear la instancia de la app.
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='clavemuysecreta',
        DATABASE=os.path.join(app.instance_path, 'pycmic_server.sqlite'),
        # Activamos el modo desarrollo de momento
        ENV='development',
    )

    if test_config is None:
        # Cargar la configuración de la aplicación (si existe)
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Si estamos en modo test no cargar la configuración
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    @app.route('/status')
    def status():
        data = {
            'status': 'ok'
        }
        return jsonify(data)
        
    return app