"""
Main FastAPI application for Instant Translation
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline
import logging
from config import HOST, PORT, DEBUG, HF_MODELS, LANGUAGES

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Instant Translation API",
    description="Real-time translation API for live streams and videos",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load translation models
translation_models = {}

def load_model(model_name: str):
    """Load a translation model from Hugging Face"""
    if model_name not in translation_models:
        try:
            logger.info(f"Loading model: {model_name}")
            model = pipeline("translation", model=model_name)
            translation_models[model_name] = model
        except Exception as e:
            logger.error(f"Error loading model {model_name}: {str(e)}")
            raise
    return translation_models[model_name]

# Request/Response Models
class TranslationRequest(BaseModel):
    text: str
    source_lang: str
    target_lang: str

class TranslationResponse(BaseModel):
    original_text: str
    translated_text: str
    source_lang: str
    target_lang: str

class HealthResponse(BaseModel):
    status: str
    version: str

# Routes
@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return {
        "status": "ok",
        "version": "1.0.0"
    }

@app.get("/languages")
async def get_languages():
    """Get list of supported languages"""
    return LANGUAGES

@app.post("/translate", response_model=TranslationResponse)
async def translate(request: TranslationRequest):
    """
    Translate text from source language to target language
    
    Example:
    {
        "text": "Hello, how are you?",
        "source_lang": "en",
        "target_lang": "es"
    }
    """
    try:
        # Validate languages
        if request.source_lang not in LANGUAGES:
            raise HTTPException(
                status_code=400,
                detail=f"Source language '{request.source_lang}' not supported"
            )
        
        if request.target_lang not in LANGUAGES:
            raise HTTPException(
                status_code=400,
                detail=f"Target language '{request.target_lang}' not supported"
            )
        
        # Get model key
        model_key = f"{request.source_lang}-{request.target_lang}"
        
        if model_key not in HF_MODELS:
            raise HTTPException(
                status_code=400,
                detail=f"Translation from {request.source_lang} to {request.target_lang} not available"
            )
        
        # Load model and translate
        model_name = HF_MODELS[model_key]
        translator = load_model(model_name)
        
        result = translator(request.text, max_length=512)
        translated_text = result[0]['translation_text']
        
        return {
            "original_text": request.text,
            "translated_text": translated_text,
            "source_lang": request.source_lang,
            "target_lang": request.target_lang
        }
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Translation error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Translation error: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    logger.info(f"Starting Instant Translation API on {HOST}:{PORT}")
    uvicorn.run(app, host=HOST, port=PORT, reload=DEBUG)
