import os


class Config(object):
    debug = True
    SECRET_KEY = os.environ.get("SECRET_KEY")

    migration_directory = "migrations"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{os.environ.get("POSTGRES_USER")}:{os.environ.get("POSTGRES_PASSWORD")}@db/{os.environ.get("POSTGRES_DB")}'

    API_PROTOCOL = os.environ.get("API_PROTOCOL")
    API_HOSTNAME = os.environ.get("API_HOSTNAME")

    FRONTEND_PROTOCOL = os.environ.get("FRONTEND_PROTOCOL")
    FRONTEND_HOSTNAME = os.environ.get("FRONTEND_HOSTNAME")

    FRONTEND_HOME = f"{FRONTEND_PROTOCOL}://{FRONTEND_HOSTNAME}/"

    TWITCH_CLIENT_ID = os.environ.get("TWITCH_CLIENT_ID")
    TWITCH_CLIENT_SECRET = os.environ.get("TWITCH_CLIENT_SECRET")

    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
