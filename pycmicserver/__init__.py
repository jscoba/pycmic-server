
from flask import Flask, jsonify
import os
import logging
from logging.handlers import RotatingFileHandler


def create_app(test_config=None):
    # crear la instancia de la app.
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='clavemuysecreta',
        DATABASE=os.path.join(app.instance_path, 'pycmic_server.sqlite'),
        # Activamos el modo desarrollo de momento
        DEBUG=True,
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

    from . import views
    app.register_blueprint(views.bp)

    # Configuración del log a archivos
    if test_config is None:
        handler = RotatingFileHandler(os.path.join(app.instance_path, 'pycmiclog.txt'), maxBytes=10000, backupCount=1)
        handler.setLevel(logging.INFO)
        app.logger.addHandler(handler)
        app.logger.info('Iniciando aplicación')
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.DEBUG)
        log.addHandler(handler)

    # Rutas de estado de la aplicación
    @app.route('/status')
    def status():
        data = {
            'status': 'ok',
            "ejemplo": { 
                "ruta": "/info",
                "valor": '{"author":"jscoba","description":"Accountability for Ricoh printesr made easy","license":"Apache 2","name":"pycmic-server","repo":"https://github.com/jscoba/pycmic-server"}'
              }
        }
        return jsonify(data)

    @app.route('/info')
    def info():
        data = {
            'name': 'pycmic-server',
            'author': 'jscoba',
            'repo': 'https://github.com/jscoba/pycmic-server',
            'license': 'Apache 2',
            'description': 'Accountability for Ricoh printesr made easy'
        }
        return jsonify(data)

    return app