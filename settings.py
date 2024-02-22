import os
from load_dotenv import load_dotenv

# *****************************
# Environment specific settings
# *****************************

load_dotenv()

DEBUG = True

POSTGRES_PORT =     os.getenv('DATABASE_PORT', 5433)
POSTGRES_USER =     os.getenv('DATABASE_USER', 'postgres')
POSTGRES_DB =       os.getenv('DATABASE_DB', 'archlimpa')
POSTGRES_PASSWORD = os.getenv('DATABASE_PASSWORD', '1234')
POSTGRES_HOST =     os.getenv('DATABASE_HOST', 'localhost')