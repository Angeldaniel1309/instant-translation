# 📱 Guía Completa: Compilar e Instalar APK - Instant Translation

## 🎯 Objetivo Final
Tener la aplicación **Instant Translation** instalada en tu teléfono Android y funcionando.

---

## 📋 PASO 1: Requisitos Previos

### Instala lo siguiente en tu computadora:

#### 1️⃣ **Java Development Kit (JDK) 11+**
- Descarga: https://www.oracle.com/java/technologies/downloads/
- Versión recomendada: **JDK 11 o 17**
- Verifica instalación:
  ```bash
  java -version
  javac -version
  ```

#### 2️⃣ **Android Studio**
- Descarga: https://developer.android.com/studio
- Instalación estándar (siguiente, siguiente, siguiente)
- Al abrir, instala los componentes que pide

#### 3️⃣ **Git**
- Descarga: https://git-scm.com/download
- Instalación estándar

#### 4️⃣ **Node.js** (opcional, pero recomendado)
- Descarga: https://nodejs.org/
- Versión: LTS (14+ en adelante)

---

## 🚀 PASO 2: Clonar el Repositorio

### Abre Terminal/CMD y ejecuta:

```bash
# Navega a donde quieras guardar el proyecto
cd C:\Users\TuUsuario\Desktop  # Windows
# o
cd ~/Desktop  # Mac/Linux

# Clona el repositorio
git clone https://github.com/Angeldaniel1309/instant-translation.git

# Entra a la carpeta
cd instant-translation
```

---

## ⚙️ PASO 3: Configurar el Backend (Servidor Python)

### 3.1 Crear Entorno Virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 3.2 Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 3.3 Ejecutar Servidor

```bash
python main.py
```

**Verás algo como:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

✅ **¡El servidor está corriendo en puerto 8000!**

---

## 📱 PASO 4: Configurar la APP para Android

### 4.1 Obtener tu IP Local

#### En Windows (CMD):
```bash
ipconfig
```
Busca "Dirección IPv4:" bajo "Ethernet" o "WiFi". Ejemplo: `192.168.1.100`

#### En Mac/Linux (Terminal):
```bash
ifconfig
```
Busca "inet" bajo "en0" o "en1". Ejemplo: `192.168.1.100`

### 4.2 Actualizar URL en la App

Abre el archivo: `mobile/android/app/src/main/java/com/instanttranslation/MainActivity.java`

Busca esta línea:
```java
private String API_URL = "http://192.168.1.100:8000";
```

Cambia `192.168.1.100` por **tu IP local**. Ejemplo:
```java
private String API_URL = "http://192.168.1.50:8000";
```

---

## 🔨 PASO 5: Compilar la APK en Android Studio

### 5.1 Abrir Proyecto en Android Studio

1. **Abre Android Studio**
2. **File → Open → Selecciona la carpeta `instant-translation/mobile/android`**
3. Espera a que Gradle sincronice (puede tardar 2-3 minutos)

### 5.2 Compilar APK

**Opción A: Con GUI (Recomendado para principiantes)**

1. En el menú: **Build → Build Bundle(s) / APK(s) → Build APK(s)**
2. Espera a que termine (puede tardar 5-10 minutos)
3. Verás un mensaje verde: "APK(s) generated successfully"

**Opción B: Con Terminal**

```bash
cd mobile/android
./gradlew assembleRelease  # Mac/Linux
# o
gradulew.bat assembleRelease  # Windows
```

---

## 📂 PASO 6: Encontrar el APK Generado

El APK estará en:
```
instant-translation/mobile/android/app/build/outputs/apk/release/app-release.apk
```

✅ **Este es tu APK final. Guárdalo en un lugar seguro.**

---

## 📱 PASO 7: Instalar en tu Teléfono Android

### Opción A: Conexión USB (Más rápido)

1. **Conecta tu teléfono con USB a la computadora**
2. **Habilita "Modo de Desarrollador" en tu teléfono:**
   - Ve a **Ajustes → Información del dispositivo**
   - Toca 7 veces en **"Número de compilación"** (hasta que diga "Modo de desarrollador activado")
   - Regresa a **Ajustes → Opciones de desarrollador**
   - Activa **"Depuración USB"**

3. **Instala el APK desde Terminal:**
   ```bash
   adb install -r app-release.apk
   ```

### Opción B: Transferencia Manual (Más fácil)

1. **Copia el APK a tu teléfono** (por USB o nube)
2. **Abre el gestor de archivos en tu teléfono**
3. **Toca el archivo `.apk`**
4. **Tapa en "Instalar"**
5. **Si pide permiso**, ve a **Ajustes → Seguridad → Instalar desde fuentes desconocidas → Activar**

---

## ✅ PASO 8: Usar la App

### Primer uso:

1. **Abre "Instant Translation" en tu teléfono**
2. **Asegúrate de que el servidor Python sigue corriendo** en tu computadora
3. **Asegúrate de estar en la MISMA RED WiFi** que tu computadora
4. **Selecciona idiomas de origen y destino**
5. **Ingresa texto o URL**
6. **Toca "🎬 Traducir Ahora"**
7. **¡Listo! Verás la traducción en segundos**

---

## 🐛 Troubleshooting

### ❌ "Error de conexión al servidor"

**Solución:**
- Verifica que ambos dispositivos estén en la MISMA WiFi
- Revisa que la IP en MainActivity.java sea correcta
- Asegúrate que el servidor Python esté corriendo (`python main.py`)
- Abre firewall en tu computadora si es necesario

### ❌ "No se puede instalar el APK"

**Solución:**
- Activa "Instalar desde fuentes desconocidas" en tu teléfono
- Asegúrate de tener espacio libre (mínimo 50MB)
- Intenta desinstalar versión anterior primero

### ❌ "APK no se compila en Android Studio"

**Solución:**
- Limpia el proyecto: **Build → Clean Project**
- Sincroniza Gradle: **File → Sync Now**
- Reinstala SDK: **Tools → SDK Manager → Instala Android 12.0 (API 31)+**

### ❌ "La app se abre pero no traduce"

**Solución:**
- Abre Terminal y verifica que el servidor esté corriendo:
  ```bash
  python main.py
  ```
- Revisa los logs del servidor en Terminal
- Asegúrate de estar en la misma WiFi

---

## 🎉 ¡Listo!

Ya tienes **Instant Translation** instalado y funcionando en tu teléfono.

### Próximas mejoras:
- ✨ Captura automática de subtítulos de YouTube
- ✨ Modo offline con modelos locales
- ✨ Compartir traducciones
- ✨ Temas personalizados

---

**¿Necesitas ayuda?** Revisa los logs del servidor o contacta al desarrollador.

**Creado por:** Angeldaniel1309  
**Versión:** 1.0.0  
**Última actualización:** 2026-09-09
