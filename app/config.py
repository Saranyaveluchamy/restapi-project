import os


class Config:
    user_name: str = os.environ.get('DB_USER', None)
    password: str = os.environ.get('DB_PASS', None)
    host: str = os.environ.get('DB_HOST', None)
    db_name: str = os.environ.get('DB_NAME', None)
    port: int = int(os.environ.get('DB_PORT', '5432'))

    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(user_name,
                                                                   password,
                                                                   host, port,
                                                                   db_name)
    DEBUG = True  # Turns on debugging features in Flask
    DEVELOPMENT = True

