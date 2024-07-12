from flask import Flask
from celery import Celery

def make_celery(app):
    celery = Celery(
        app.import_name,
        broker=app.config['CELERY_BROKER_URL'],
        backend=app.config['CELERY_RESULT_BACKEND']
    )
    celery.conf.update(app.config)
    return celery

def create_app():
    app = Flask(__name__)
    app.config.update(
        CELERY_BROKER_URL='amqp://localhost//',
        CELERY_RESULT_BACKEND='rpc://'
    )

    from .main import app as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

app = create_app()
celery = make_celery(app)
