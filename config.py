import os
from dotenv import find_dotenv,load_dotenv
load_dotenv(find_dotenv())
# API Keys
GROQ_API_KEY = os.environ['GROQ_API_KEY']
# Directories
IMAGE_DIR = "extracted_images"
os.makedirs(IMAGE_DIR, exist_ok=True)
