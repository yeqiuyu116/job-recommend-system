# 数据库的配置信息
from sqlalchemy.testing.provision import drop_db

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE ='big_data_base'
USERNAME ='root'
PASSWORD ='123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME,PASSWORD, HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
