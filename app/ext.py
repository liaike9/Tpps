from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

def init_ext(app):
    init_db(app)
    # 邮箱注册
    init_mail(app)
    pass


# 配置数据库orm 框架
db = SQLAlchemy()
# 数据库迁移
migrate = Migrate()
# 初始化数据库配置
def init_db(app):
    db.init_app(app=app)
    migrate.init_app(app, db)

# 配置邮箱
mail = Mail()

def init_mail(app):
     mail.init_app(app)
