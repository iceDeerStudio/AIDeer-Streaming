import os
from dotenv import load_dotenv
from datetime import timedelta

# Load environment variables from .env file
load_dotenv()

class Config:
    HOST = os.getenv('HOST')
    PORT = os.getenv('PORT')
    RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')
    RABBITMQ_PORT = os.getenv('RABBITMQ_PORT')
    RABBITMQ_USER = os.getenv('RABBITMQ_USER')
    RABBITMQ_PASSWD = os.getenv('RABBITMQ_PASSWD')