import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

DOWNLOADS_DIR = 'downloads'
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos')  # under_DOWNLOADS_DIR
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'captions')  # under_DOWNLOADS_DIR
OUTPUTS_DIR = 'outputs'
