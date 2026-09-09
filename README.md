# Instant Translation 🌐

**Traductor instantáneo en tiempo real para streams y videos en vivo**

Traduce contenido de YouTube, Kick, Twitch y otras plataformas al instante. Captura el audio/subtítulos en vivo y los traduce a español, inglés, portugués, francés y más idiomas, mostrando un overlay con subtítulos traducidos.

## 🚀 Características

- ✅ Traducción en tiempo real sin demora
- ✅ Soporte multi-idioma (Español, Inglés, Portugués, Francés, Italiano, Alemán, etc.)
- ✅ API gratuita (Hugging Face)
- ✅ Overlay de subtítulos traducidos
- ✅ Integración con YouTube, Kick, Twitch
- ✅ Interfaz oscura y moderna
- ✅ Bajo uso de recursos

## 📋 Requisitos

- Python 3.8+
- Node.js 14+ (para frontend)
- Hugging Face API (gratuita)

## 🛠️ Instalación

### Backend (Python)

```bash
# Clonar repositorio
git clone https://github.com/Angeldaniel1309/instant-translation.git
cd instant-translation

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor
python main.py
```

### Frontend (React)

```bash
cd frontend
npm install
npm start
```

## 📖 Uso

1. Abre tu navegador en `http://localhost:3000`
2. Ingresa la URL del video/stream
3. Selecciona el idioma de origen y destino
4. ¡Haz clic en "Traducir"!
5. Los subtítulos aparecerán en tiempo real

## 🌐 Idiomas Soportados

- 🇪🇸 Español
- 🇬🇧 Inglés
- 🇧🇷 Portugués
- 🇫🇷 Francés
- 🇮🇹 Italiano
- 🇩🇪 Alemán
- Y más...

## 🤖 Tecnología

- **Backend:** Python (FastAPI/Flask)
- **Frontend:** React.js
- **IA:** Hugging Face Transformers
- **API de Traducción:** Helsinki-NLP (Opus-MT)

## 📄 Licencia

MIT License - ver LICENSE para detalles

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor abre un issue o pull request.

---

**Creado por:** Angeldaniel1309  
**Estado:** En desarrollo 🚀
