@echo off
REM Instant Translation - Script de Instalación Rápida (Windows)

echo 🚀 Instalando Instant Translation...

REM Verificar Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python no está instalado. Descárgalo de https://python.org
    pause
    exit /b 1
)

echo ✅ Python encontrado: 
for /f "tokens=*" %%i in ('python --version') do echo %%i

REM Crear entorno virtual
echo 📦 Creando entorno virtual...
python -m venv venv
call venv\Scripts\activate.bat

REM Instalar dependencias
echo 📥 Instalando dependencias...
pip install --upgrade pip
pip install -r requirements.txt

REM Copiar .env
echo ⚙️ Configurando variables...
if not exist .env (
    copy .env.example .env
    echo 📝 Archivo .env creado. Edítalo según sea necesario.
)

echo.
echo ✅ ¡Instalación completada!
echo.
echo 🚀 Para ejecutar el servidor, usa:
echo    venv\Scripts\activate.bat
echo    python main.py
echo.
echo 📱 Luego, configura la app Android con tu IP local.
echo.
pause
