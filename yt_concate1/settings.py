import os
from dotenv import dotenv_values
config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}
API_KEY = os.getenv('API_KEY')
