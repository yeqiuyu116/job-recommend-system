from flask import Flask
import config
from exts import db
from flask_cors import CORS
import json
from datetime import datetime

from controller.UserController import user as user_blueprint
from controller.SysUserController import sysUser as sysUser_blueprint

app = Flask(__name__)
app.config.from_object(config)
CORS(app)

db.init_app(app)

app.register_blueprint(user_blueprint)
app.register_blueprint(sysUser_blueprint)


if __name__ == '__main__':
    app.run()
