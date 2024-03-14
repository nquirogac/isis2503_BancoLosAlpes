from dotenv import load_dotenv
import os

load_dotenv()
RABBIT_HOST=os.getenv('RABBIT_HOST')
RABBIT_USER=os.getenv('RABBIT_USER')
RABBIT_PASSWORD=os.getenv('RABBIT_PASSWORD')
