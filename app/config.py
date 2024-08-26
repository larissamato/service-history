import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_DATABASE = os.getenv('DB_DATABASE')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'


API_URL = os.getenv('API_URL')
API_TOKEN = os.getenv('API_TOKEN')
INITIAL_DATE = os.getenv('INITIAL_DATE')

HEADERS = {
    'accept': 'application/json',
    'Authorization': API_TOKEN
}
