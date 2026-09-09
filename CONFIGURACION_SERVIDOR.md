# 🖥️ Configuración del Servidor FastAPI

## 📋 Requisitos

- Python 3.8+
- pip (gestor de paquetes de Python)
- Conexión a Internet

---

## 🚀 Instalación Rápida

### 1. Crear Entorno Virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar Variables de Entorno

```bash
# Copiar archivo de ejemplo
cp .env.example .env

# Editar .env con tu editor favorito y cambiar:
DEBUG=True
HOST=0.0.0.0
PORT=8000
```

### 4. Ejecutar Servidor

```bash
python main.py
```

**Output esperado:**
```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete
INFO:     Uvicorn running on http://0.0.0.0:8000
```

---

## 📡 Probar la API

### Verificar Salud del Servidor

```bash
curl http://localhost:8000/health
```

**Respuesta:**
```json
{"status":"ok","version":"1.0.0"}
```

### Obtener Idiomas Disponibles

```bash
curl http://localhost:8000/languages
```

**Respuesta:**
```json
{
  "en": "English",
  "es": "Español",
  "pt": "Português",
  "fr": "Français",
  "it": "Italiano",
  "de": "Deutsch"
}
```

### Traducir Texto

```bash
curl -X POST http://localhost:8000/translate \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Hello, how are you?",
    "source_lang": "en",
    "target_lang": "es"
  }'
```

**Respuesta:**
```json
{
  "original_text": "Hello, how are you?",
  "translated_text": "Hola, ¿cómo estás?",
  "source_lang": "en",
  "target_lang": "es"
}
```

---

## 🔌 Conectar desde la APP Android

### En Android Studio, actualiza MainActivity.java:

```java
private String API_URL = "http://192.168.1.100:8000"; // Cambia por tu IP
```

### Obtener tu IP Local:

**Windows (CMD):**
```bash
ipconfig
```
Busca "IPv4 Address"

**Mac/Linux (Terminal):**
```bash
ifconfig
```
Busca "inet"

---

## ⚙️ Configuración Avanzada

### Cambiar Puerto

En `.env`:
```
PORT=9000
```

### Agregar Más Idiomas

En `config.py`, agregar al diccionario `HF_MODELS`:

```python
HF_MODELS = {
    "en-es": "Helsinki-NLP/opus-mt-en-es",
    "es-en": "Helsinki-NLP/opus-mt-es-en",
    "en-de": "Helsinki-NLP/opus-mt-en-de",  # Nuevo
    "de-en": "Helsinki-NLP/opus-mt-de-en",  # Nuevo
}
```

### Usar API Key de Hugging Face

1. Crea cuenta en https://huggingface.co
2. Genera API Key
3. En `.env`:
   ```
   HF_API_KEY=hf_xxxxxxxxxxxxxxxxxxxxx
   ```

---

## 🐛 Solucionar Problemas

### "ModuleNotFoundError: No module named 'fastapi'"

```bash
# Instala dependencias de nuevo
pip install -r requirements.txt
```

### "Port 8000 already in use"

```bash
# Usa otro puerto
PORT=9000 python main.py
```

### "Model download failed"

```bash
# Descarga el modelo manualmente
python -c "from transformers import pipeline; pipeline('translation', model='Helsinki-NLP/opus-mt-en-es')"
```

---

## 📊 Monitoreo

Para ver logs detallados:

```bash
DEBUG=True python main.py
```

---

**Creado por:** Angeldaniel1309  
**Última actualización:** 2026-09-09
