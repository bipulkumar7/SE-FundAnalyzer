from flask import Config
    
class DevConfig(Config):
  debug = True 
  SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:asdert123@localhost:3306/cf"
