# Tikun Framework - Backend API

API backend para Tikun Framework, desplegable en Render.

## Estructura del Proyecto

```
tikun_backend/
├── api_server.py          # FastAPI server principal
├── tikun_orchestrator.py  # Orquestador de las 10 Sefirot
├── sefirot/               # Módulos de análisis
├── requirements.txt       # Dependencias Python
├── render.yaml           # Configuración para Render
├── runtime.txt           # Versión de Python
└── .env                  # Variables de entorno (local)
```

## Variables de Entorno Requeridas

Crea un archivo `.env` en la raíz con:

```env
GOOGLE_API_KEY=tu_clave_google_aqui
DEEPSEEK_API_KEY=tu_clave_deepseek_aqui
MISTRAL_API_KEY=tu_clave_mistral_aqui
```

### Cómo Obtener las API Keys

1. **Google Gemini**: https://makersuite.google.com/app/apikey (Gratis con límites generosos)
2. **DeepSeek**: https://platform.deepseek.com/ (Muy económico, ~$0.14/M tokens)
3. **Mistral**: https://console.mistral.ai/ (Gratis con créditos iniciales)

### Distribución de LLMs por Sefirot

El framework usa principalmente Gemini (gratis) con Mistral y DeepSeek para módulos específicos:

- **Gemini** (8 Sefirot): Keter, Chesed, Gevurah, Tiferet, Netzach, Hod, Yesod, Malchut, BinahSigma Occidente
- **Mistral** (1 Sefira): Chochmah
- **DeepSeek** (1 Sefira): BinahSigma Oriente

Esta distribución optimiza costos (la mayoría usa Gemini gratis) y calidad de análisis.

## Instalación Local

1. Crear entorno virtual:
```bash
python -m venv venv
```

2. Activar entorno virtual:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecutar servidor:
```bash
python api_server.py
```

El servidor estará disponible en: http://localhost:8000

## Documentación API

Una vez el servidor esté corriendo:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Despliegue en Render

### Opción 1: Usando render.yaml (Recomendado - GRATIS)

1. Sube tu código a GitHub (si aún no lo has hecho):
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/tu-usuario/tikun-backend.git
git push -u origin main
```

2. Ve a [Render Dashboard](https://dashboard.render.com/)

3. Click en "New +" → "Blueprint"

4. Conecta tu repositorio de GitHub

5. Render detectará automáticamente el `render.yaml` y configurará el servicio **en el tier GRATUITO**

6. Agrega las variables de entorno en el dashboard:
   - `GOOGLE_API_KEY`
   - `DEEPSEEK_API_KEY`
   - `MISTRAL_API_KEY`

7. Click en "Apply" para desplegar

### Opción 2: Configuración Manual

1. Ve a [Render Dashboard](https://dashboard.render.com/)

2. Click en "New +" → "Web Service"

3. Conecta tu repositorio de GitHub

4. Configura:
   - **Name**: `tikun-backend`
   - **Environment**: `Python 3`
   - **Plan**: **Free** (IMPORTANTE: Selecciona el plan gratuito)
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn api_server:app --host 0.0.0.0 --port $PORT`

5. Variables de entorno:
   - Agrega `GOOGLE_API_KEY`, `DEEPSEEK_API_KEY`, `MISTRAL_API_KEY`

6. Click en "Create Web Service"

### Después del Despliegue

Una vez desplegado, tu API estará disponible en:
```
https://tikun-backend.onrender.com
```

Actualiza tu frontend en Firebase para usar esta URL en lugar de `localhost:8000`.

## Endpoints Principales

### POST /api/analyze
Inicia un análisis Tikun en background.

```javascript
const response = await fetch('https://tikun-backend.onrender.com/api/analyze', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        scenario: "PROPUESTA: Implementar...",
        case_name: "Demo_Case"
    })
});
const { job_id } = await response.json();
```

### GET /api/status/{job_id}
Verifica el estado del análisis.

```javascript
const response = await fetch(`https://tikun-backend.onrender.com/api/status/${jobId}`);
const status = await response.json();
```

### GET /api/results/{job_id}
Obtiene los resultados cuando el análisis está completo.

```javascript
const response = await fetch(`https://tikun-backend.onrender.com/api/results/${jobId}`);
const results = await response.json();
```

## Actualizar Frontend

En tu frontend de Firebase, actualiza la URL base de la API:

```javascript
// Antes (local)
const API_URL = 'http://localhost:8000';

// Después (producción)
const API_URL = 'https://tikun-backend.onrender.com';
```

## Troubleshooting

### Error: "Module not found"
- Asegúrate de que `requirements.txt` esté actualizado
- Verifica que el build command en Render sea: `pip install -r requirements.txt`

### Error: CORS
- Verifica que `https://tikunframework.web.app` esté en `allow_origins` en `api_server.py`
- Si cambias el dominio de Firebase, actualiza el CORS

### Timeout en Render (free tier)
- Los servicios gratuitos de Render se duermen después de 15 minutos de inactividad
- La primera request después del sleep puede tardar 30-60 segundos
- Considera usar un servicio de "keep-alive" o upgrade a plan pagado

## Monitoreo

- **Logs**: Dashboard de Render → Tu servicio → "Logs"
- **Métricas**: Dashboard de Render → Tu servicio → "Metrics"
- **Health Check**: `https://tikun-backend.onrender.com/` debería retornar status 200

## Notas Importantes

- **Free Tier de Render**: El servicio puede dormirse después de inactividad
- **Límites de API**: Configura rate limiting para las API keys de OpenAI/Anthropic
- **Seguridad**: NUNCA commitas el archivo `.env` al repositorio
- **Almacenamiento**: Los resultados se guardan en memoria (se pierden al reiniciar). Para persistencia, considera usar Redis o PostgreSQL

## Soporte

Para problemas con el despliegue, consulta:
- [Render Documentation](https://render.com/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
