import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'asla-tahmin-edemezsin'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(os.path.dirname(__file__), 'app.db')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False