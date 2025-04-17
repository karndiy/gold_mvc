from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app = Flask(__name__, template_folder='views/templates') 
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '../gold.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.controllers.gold_controller import gold_bp
    app.register_blueprint(gold_bp)

    with app.app_context():
        from app.models import gold_model
        db.create_all()

    return app
