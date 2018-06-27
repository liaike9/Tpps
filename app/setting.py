class Config():
    DEBUG = False
    SECRET_KEY = 'aefe8fded8724467b3741af506434ccd'


# 生成数据库链接
def get_db_uri(database: dict):
    user = database.get('USER') or 'root'
    password = database.get('PASSWORD') or '123456'
    host = database.get('HOST') or '127.0.0.1'
    port = database.get('PORT') or '3306'
    name = database.get('NAME')
    db = database.get('DB') or 'mysql'
    driver = database.get('DRIVER') or 'pymysql'
    charset = database.get('CHARSET') or 'utf8'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/tpp'
    return '{}+{}://{}:{}@{}:{}/{}?charset={}'.format(db, driver, user, password, host, port, name, charset)


# 开发环境搭建
class DevelopConfig(Config):
    DEBUG = True

    DATABASE = {
        'NAME': 'tpp'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/taopp'
    # 发送邮箱配置
    MAIL_SERVER = 'smtp.163.com'  # 邮箱服务器
    # MAIL_PORT = 110
    MAIL_USERNAME = '17608293569@163.com'
    MAIL_PASSWORD = 'like1234567'  # 授权码


# 项目上线配置
class ProductConfig(Config):
    DEBUG = True
    DATABASE = {
        'DB': 'mysql',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'tpp',
        'DRIVER': 'pymysql',
        'CHARSET': 'utf8',
    }
    # 配置数据库连接
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/taopp'
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


env = {
    # 开发环境
    'dev': DevelopConfig,
    # 生产环境
    'pro': ProductConfig,
}
