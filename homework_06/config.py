from os import getenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DEFAULT_DB_URL = "postgresql+psycopg2://username:passwd@0.0.0.0:5432/app"

SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    DEFAULT_DB_URL,
)


class Config:
    TESTING = False
    DEBUG = False
    SECRET_KEY = "e4de2b570761b7a6ce1efb624f848425"
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
