from flask import Flask

from app.apis import register_blue
from app.ext import init_ext

from app.setting import env


app = Flask(__name__)


def create_app(env_name):
    # 从配置对象中加载配置
    app.config.from_object(env.get(env_name))
    # 初始化
    init_ext(app)
    # 注册蓝图
    register_blue(app)
    return app

