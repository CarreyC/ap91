from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from apple.config import Config

import redis

db = SQLAlchemy()
rs = redis.StrictRedis(host='redis', port=6379, charset='utf-8', decode_responses=True)
bs = Bootstrap()
bcrypt = Bcrypt()

# login_manager = LoginManager()
# login_manager.login_view = 'ucenter.index'
# login_manager.login_message_category = 'info'

app = Flask(__name__)

def create_app():
    config = Config()
    app.config.from_object(config)

    db.init_app(app)
    bcrypt.init_app(app)
    # login_manager.init_app(app)

    from apple.trade.routes import trade

    app.register_blueprint(trade)

    return app
