from app import get_app
from config import TestingConfig


def get():
    return get_app(TestingConfig)
