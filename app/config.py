import os
import dotenv
import secrets

dotenv.load_dotenv()

BASE_DIR = os.path.dirname(__file__)

class Config():

    SECRET_KEY = os.getenv('SECRET_KEY', secrets.token_hex(20))
