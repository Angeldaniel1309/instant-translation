"""
Configuration file for Instant Translation
"""

import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
DEBUG = os.getenv("DEBUG", "True") == "True"
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))

# Hugging Face Configuration
HF_MODEL_NAME = "Helsinki-NLP/opus-mt-en-es"  # English to Spanish
HF_MODELS = {
    "en-es": "Helsinki-NLP/opus-mt-en-es",      # English to Spanish
    "es-en": "Helsinki-NLP/opus-mt-es-en",      # Spanish to English
    "en-pt": "Helsinki-NLP/opus-mt-en-pt",      # English to Portuguese
    "pt-en": "Helsinki-NLP/opus-mt-pt-en",      # Portuguese to English
    "en-fr": "Helsinki-NLP/opus-mt-en-fr",      # English to French
    "fr-en": "Helsinki-NLP/opus-mt-fr-en",      # French to English
}

# Supported Languages
LANGUAGES = {
    "en": "English",
    "es": "Español",
    "pt": "Português",
    "fr": "Français",
    "it": "Italiano",
    "de": "Deutsch",
}

# Audio Configuration
SAMPLE_RATE = 16000
CHUNK_SIZE = 1024

# Timeout Configuration
TRANSLATION_TIMEOUT = 30  # seconds
