# Flask settings
FLASK_SERVER_NAME = 'localhost:8888'
FLASK_DEBUG = True  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

# Database Details
DB_USER = 'dmu_nasisha'
DB_PASSWORD = 'Axtria@0620'
DB_SERVER = '172.31.47.186'
DB_DATABASE = 'pg_datamax_dev'
PG_SCHEMA = 'dmu_nasisha'
DB_URI= f'postgres://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:5432/{DB_DATABASE}'

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
