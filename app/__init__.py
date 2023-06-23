import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    db_user=os.environ.get('DB_USER')
    db_pass=os.environ.get('DB_PASSWORD')
    db_host=os.environ.get('DB_HOST')
    db_name=os.environ.get('DB_NAME')

    DATABASE_URL = f"postgresql://{db_user}:{db_pass}@{db_host}/{db_name}"

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)

    from .models import user

    from .views import root_bp, authenticate_bp
    
    app.register_blueprint(root_bp, url_prefix='/')
    app.register_blueprint(authenticate_bp)


    return app