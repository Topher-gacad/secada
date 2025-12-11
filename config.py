import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    REQUIRED_ENV_VARS = ['DB_USER', 'DB_PASSWORD', 'DB_HOST', 'DB_NAME']

    @staticmethod
    def validate_env():
        missing = [var for var in Config.REQUIRED_ENV_VARS if not os.getenv(var)]
        if missing:
            raise EnvironmentError(
                f"Missing required environment variables: {', '.join(missing)}\n"
                f"Please check your .env file"
            )
        
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False