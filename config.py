import os

# API Keys
os.environ["GROQ_API_KEY"] = "YOUR_API_KEY"

# Directories
IMAGE_DIR = "extracted_images"
os.makedirs(IMAGE_DIR, exist_ok=True)
