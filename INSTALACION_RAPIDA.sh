#!/bin/bash

# Instant Translation - Script de Instalación Rápida
# Este script instala y configura todo automáticamente

echo "🚀 Instalando Instant Translation..."

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no está instalado. Descárgalo de https://python.org"
    exit 1
fi

echo "✅ Python encontrado: $(python3 --version)"

# Crear entorno virtual
echo "📦 Creando entorno virtual..."
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
echo "📥 Instalando dependencias..."
pip install --upgrade pip
pip install -r requirements.txt

# Copiar .env
echo "⚙️ Configurando variables..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "📝 Archivo .env creado. Edítalo según sea necesario."
fi

echo ""
echo "✅ ¡Instalación completada!"
echo ""
echo "🚀 Para ejecutar el servidor, usa:"
echo "   source venv/bin/activate"
echo "   python main.py"
echo ""
echo "📱 Luego, configura la app Android con tu IP local."
echo ""
