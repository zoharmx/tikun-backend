# 🚀 Guía Rápida de Despliegue en Render (GRATIS)

## ✅ Pre-requisitos

Antes de comenzar, asegúrate de tener:

1. Una cuenta en [GitHub](https://github.com) (gratis)
2. Una cuenta en [Render](https://render.com) (gratis)
3. Las API keys de:
   - Google Gemini (gratis)
   - DeepSeek (muy económico, ~$0.14/M tokens)
   - Mistral (gratis con créditos iniciales)

---

## 📝 Paso 1: Obtener las API Keys

### 1.1 Google Gemini (GRATIS)
1. Ve a: https://makersuite.google.com/app/apikey
2. Inicia sesión con tu cuenta Google
3. Click en "Create API Key"
4. Copia y guarda la clave

### 1.2 DeepSeek (Muy económico)
1. Ve a: https://platform.deepseek.com/
2. Regístrate con tu email
3. Ve a "API Keys" en el dashboard
4. Click en "Create API Key"
5. Copia y guarda la clave
6. Recarga créditos (desde $1 USD)

### 1.3 Mistral (Créditos gratis)
1. Ve a: https://console.mistral.ai/
2. Regístrate con tu email
3. Verifica tu cuenta
4. Ve a "API Keys"
5. Click en "Create new key"
6. Copia y guarda la clave

---

## 📦 Paso 2: Subir a GitHub

1. **Crea un nuevo repositorio en GitHub**:
   - Ve a https://github.com/new
   - Nombre: `tikun-backend`
   - Visibilidad: Private (recomendado) o Public
   - NO inicialices con README
   - Click en "Create repository"

2. **Sube tu código** (ejecuta en tu terminal):

```bash
# Ya tienes git init hecho, solo necesitas:
git remote add origin https://github.com/TU-USUARIO/tikun-backend.git
git branch -M main
git push -u origin main
```

Reemplaza `TU-USUARIO` con tu nombre de usuario de GitHub.

---

## 🌐 Paso 3: Desplegar en Render (GRATIS)

### Opción A: Blueprint (Recomendado - Automático)

1. Ve a: https://dashboard.render.com/

2. Click en **"New +"** → **"Blueprint"**

3. **Conecta tu repositorio de GitHub**:
   - Si es tu primera vez, autoriza a Render
   - Busca y selecciona `tikun-backend`

4. Render detectará automáticamente el archivo `render.yaml`

5. **IMPORTANTE**: Verifica que diga **"Free"** en el plan
   - Si dice "$7/month", NO continúes
   - Cancela y usa la Opción B (Manual)

6. **Agrega las variables de entorno**:
   - Click en "Environment" o "Advanced"
   - Agrega estas 3 variables:
     ```
     GOOGLE_API_KEY = [pega tu clave de Gemini]
     DEEPSEEK_API_KEY = [pega tu clave de DeepSeek]
     MISTRAL_API_KEY = [pega tu clave de Mistral]
     ```

7. Click en **"Apply"** o **"Deploy"**

8. Espera 5-10 minutos mientras Render construye tu servicio

### Opción B: Manual (Si Blueprint cobra)

1. Ve a: https://dashboard.render.com/

2. Click en **"New +"** → **"Web Service"**

3. **Conecta tu repositorio**:
   - Conecta GitHub si aún no lo has hecho
   - Selecciona `tikun-backend`

4. **Configura el servicio**:
   - **Name**: `tikun-backend`
   - **Environment**: `Python 3`
   - **Region**: Cualquiera (usa la más cercana)
   - **Branch**: `main`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn api_server:app --host 0.0.0.0 --port $PORT`

5. **CRÍTICO - Selecciona el plan GRATUITO**:
   - Scroll hasta "Instance Type"
   - Selecciona **"Free"**
   - NUNCA selecciones "Starter" o superior

6. **Variables de entorno**:
   - Scroll hasta "Environment Variables"
   - Click en "Add Environment Variable"
   - Agrega:
     ```
     GOOGLE_API_KEY = [tu clave]
     DEEPSEEK_API_KEY = [tu clave]
     MISTRAL_API_KEY = [tu clave]
     ```

7. Click en **"Create Web Service"**

8. Espera 5-10 minutos mientras construye

---

## ✅ Paso 4: Verificar el Despliegue

1. **Espera a que el build termine**:
   - En Render verás "Build in progress..."
   - Cuando termine, dirá "Live"

2. **Obtén tu URL**:
   - Render te dará una URL como:
     ```
     https://tikun-backend-xxxx.onrender.com
     ```
   - Copia esta URL

3. **Prueba tu API**:
   - Abre en el navegador:
     ```
     https://tikun-backend-xxxx.onrender.com/
     ```
   - Deberías ver algo como:
     ```json
     {
       "service": "Tikun Framework API",
       "version": "2.0",
       "status": "operational"
     }
     ```

4. **Accede a la documentación**:
   - Ve a:
     ```
     https://tikun-backend-xxxx.onrender.com/docs
     ```
   - Verás la interfaz Swagger con todos los endpoints

---

## 🔗 Paso 5: Conectar con tu Frontend

1. **Actualiza tu frontend en Firebase**:

   Busca donde defines la URL de la API (probablemente en un archivo como `config.js` o `constants.js`):

   ```javascript
   // Antes
   const API_URL = 'http://localhost:8000';

   // Después
   const API_URL = 'https://tikun-backend-xxxx.onrender.com';
   ```

2. **Redespliega tu frontend**:
   ```bash
   firebase deploy
   ```

3. **Prueba la conexión**:
   - Ve a: https://tikunframework.web.app/new-analysis/
   - Crea un análisis de prueba
   - Verifica que se comunique con el backend

---

## ⚠️ Limitaciones del Tier Gratuito

1. **Sleep después de inactividad**:
   - Render duerme el servicio después de 15 minutos sin requests
   - La primera request después del sleep toma 30-60 segundos
   - Las siguientes requests son instantáneas

2. **750 horas/mes**:
   - Suficiente para uso personal/demo
   - Para producción considera upgrade

3. **Solución para el sleep**:
   - Usa un servicio de "keep-alive" (ej: cron-job.org)
   - O acepta el delay inicial

---

## 🐛 Troubleshooting

### Error: "Build failed"
- Revisa los logs en Render
- Verifica que `requirements.txt` esté correcto
- Asegúrate de usar Python 3.12

### Error: CORS
- Verifica que `https://tikunframework.web.app` esté en `api_server.py`
- Si cambiaste el dominio, actualiza el código

### Error: "API Key invalid"
- Verifica que las 3 API keys estén correctas en Render
- Sin espacios antes/después
- Sin comillas

### Servicio muy lento
- Es normal la primera vez después del sleep
- Espera 30-60 segundos
- Si persiste, revisa los logs
- **Solución**: Configura keep-alive con cron-job.org (ver abajo)

---

## 📊 Monitoreo

- **Ver logs**: Dashboard de Render → Tu servicio → "Logs"
- **Métricas**: Dashboard de Render → Tu servicio → "Metrics"
- **Eventos**: Dashboard de Render → Tu servicio → "Events"

---

## 💰 Costos Estimados

Con el uso normal (100 análisis/mes):

- **Render**: $0 (tier gratuito)
- **Google Gemini**: $0 (dentro del límite gratuito)
- **DeepSeek**: ~$0.50/mes (muy económico)
- **Mistral**: $0-2/mes (créditos gratis iniciales)

**Total estimado**: $0.50-2.50/mes

---

## 🔄 BONUS: Evitar el "Sleep" del Servicio (Recomendado)

El tier gratuito de Render duerme el servicio después de 15 minutos sin uso. La primera request tarda 30-60 segundos.

### Solución: Usar Cron-Job.org (Gratis)

**SÍ**, esto resuelve completamente el problema de los requests lentos.

1. **Crea cuenta en**: https://cron-job.org/ (gratis)

2. **Crea un nuevo cronjob**:
   - **URL**: `https://tikun-backend-xxxx.onrender.com/`
   - **Schedule**: Every **10 minutes**
   - **Method**: GET

3. **Guarda** y listo

Ahora tu servicio **NUNCA** se duerme y todas las requests son instantáneas.

**Alternativa mejor**: https://uptimerobot.com/ (monitoreo + keep-alive + alertas gratis)

📖 **Guía detallada**: Lee `KEEP_ALIVE_GUIDE.md` para instrucciones paso a paso

---

## 🎉 ¡Listo!

Tu backend Tikun está desplegado y conectado a tu frontend en Firebase.

¿Problemas? Revisa:
1. Los logs en Render
2. Las variables de entorno
3. La sección de Troubleshooting arriba

¡Disfruta de Tikun Framework! 🌟
