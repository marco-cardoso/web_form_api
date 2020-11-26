from app import get_app
from config import DevelopmentConfig, ProductionConfig


application = get_app(DevelopmentConfig)

if __name__ == '__main__':
    application.run()
