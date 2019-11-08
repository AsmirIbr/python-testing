import os

db_host = os.environ.get('DB_HOST', default='lottery.cuwpfmacplol.eu-west-2.rds.amazonaws.com')
db_name = os.environ.get('DB_NAME', default='Notes')
db_user = os.environ.get('DB_USERNAME', default='admin')
db_password = os.environ.get('DB_PASSWORD', default='admin1993')
db_port = os.environ.get('DB_PORT', default='3306')

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"