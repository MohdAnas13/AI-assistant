# Flask Configuration

class Config:
    SECRET_KEY = 'your_secret_key'
    DEBUG = True
    TESTING = False
    
    # Database Settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # API Keys
    API_KEY = 'your_api_key'
    ANOTHER_API_KEY = 'another_api_key'