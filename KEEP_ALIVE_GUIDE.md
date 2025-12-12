# 🔄 Guía: Mantener el Servicio Activo (Evitar el "Sleep")

## ❓ El Problema

El tier gratuito de Render tiene una limitación:
- Después de **15 minutos sin requests**, el servicio se "duerme"
- La primera request después del sleep tarda **30-60 segundos** (cold start)
- Las siguientes requests son instantáneas

## ✅ La Solución: Cron-Job.org

**SÍ**, usar **cron-job.org** (o similar) resuelve completamente el problema. Al hacer ping periódicamente, mantienes el servicio "despierto".

---

## 🚀 Configuración Paso a Paso

### Paso 1: Crear Cuenta en Cron-Job.org

1. Ve a: https://cron-job.org/
2. Click en **"Sign Up"** (Registro gratis)
3. Completa el registro con tu email
4. Verifica tu email

### Paso 2: Crear un Cron Job

1. **Inicia sesión** en https://console.cron-job.org/

2. Click en **"Create cronjob"**

3. **Configuración del Job**:

   **Title (Título)**:
   ```
   Tikun Backend Keep-Alive
   ```

   **URL**:
   ```
   https://tikun-backend-xxxx.onrender.com/
   ```
   *(Reemplaza con tu URL real de Render)*

   **Schedule (Programación)**:
   - Selecciona: **"Every X minutes"**
   - Valor: **10 minutos**

   ⚠️ **IMPORTANTE**: Usar 10 minutos (no 15) para evitar que llegue al límite

   **Advanced Settings (Opcional pero recomendado)**:
   - **Request method**: `GET`
   - **Request timeout**: 30 segundos
   - **Execution time**: Cualquiera (ej: 00:00-23:59)

4. Click en **"Create"**

### Paso 3: Verificar que Funciona

1. Espera 10 minutos
2. En cron-job.org, ve a **"Executions"** o **"History"**
3. Deberías ver:
   ```
   ✅ Success - 200 OK
   ```

4. En Render, ve a tu servicio → **"Logs"**
5. Deberías ver requests cada 10 minutos:
   ```
   GET / 200
   ```

---

## 🎯 Alternativas a Cron-Job.org

Si prefieres otras opciones:

### 1. **UptimeRobot** (Recomendado - Más completo)
- URL: https://uptimerobot.com/
- Gratis: Hasta 50 monitores
- Intervalo mínimo: 5 minutos
- Bonus: Te notifica si el servicio cae

**Configuración**:
1. Crea cuenta en UptimeRobot
2. Click en "Add New Monitor"
3. Monitor Type: HTTP(s)
4. URL: `https://tikun-backend-xxxx.onrender.com/`
5. Monitoring Interval: 5 minutes
6. Save

### 2. **Koyeb** (Alternativa a Render)
- No tiene sleep en tier gratuito
- Pero tiene límites de horas/mes

### 3. **Ping desde tu Frontend**
Agregar en tu frontend un ping periódico:

```javascript
// En tu app de Firebase
setInterval(() => {
  fetch('https://tikun-backend-xxxx.onrender.com/')
    .catch(() => {/* ignorar errores */});
}, 10 * 60 * 1000); // cada 10 minutos
```

⚠️ **Nota**: Solo funciona mientras el usuario tenga la app abierta

---

## 📊 Comparación de Opciones

| Servicio | Intervalo Mínimo | Gratis | Monitoreo | Notificaciones |
|----------|------------------|--------|-----------|----------------|
| **Cron-Job.org** | 1 minuto | ✅ Sí | ❌ No | ❌ No |
| **UptimeRobot** | 5 minutos | ✅ Sí | ✅ Sí | ✅ Email/SMS |
| **Ping desde Frontend** | Variable | ✅ Sí | ❌ No | ❌ No |

**Recomendación**: Usa **UptimeRobot** si quieres monitoreo completo, o **Cron-Job.org** si solo necesitas keep-alive simple.

---

## 💡 Tips Adicionales

### 1. No Hagas Ping Demasiado Seguido
- **Evita**: Intervalos menores a 5 minutos
- **Razón**: Consume ancho de banda innecesario
- **Óptimo**: 10 minutos (balance perfecto)

### 2. Usa el Endpoint Raíz
```
✅ Correcto: https://tikun-backend-xxxx.onrender.com/
❌ Incorrecto: https://tikun-backend-xxxx.onrender.com/api/analyze
```
**Razón**: El endpoint raíz (`/`) es ligero y no consume recursos de las APIs de LLMs.

### 3. Verifica en los Logs de Render
Cada día, revisa que los pings estén llegando:
```
[fecha] GET / 200 - Response time: 50ms
[fecha] GET / 200 - Response time: 45ms
```

### 4. Ten en Cuenta las Horas del Tier Gratuito
- Render Free: **750 horas/mes**
- Con keep-alive 24/7: **720 horas/mes**
- **✅ Suficiente** (quedan 30 horas de margen)

---

## 🧪 Prueba del Keep-Alive

Para verificar que funciona:

1. **Espera 20 minutos** sin hacer requests manuales
2. **Haz un request** desde tu frontend
3. Si el keep-alive funciona:
   - ✅ Respuesta instantánea (< 1 segundo)
4. Si NO funciona:
   - ❌ Respuesta lenta (30-60 segundos)

---

## ⚠️ Importante: No Abuses

Aunque es gratis, respeta los términos de servicio:

- ✅ **Correcto**: Ping cada 10 minutos para uso legítimo
- ❌ **Incorrecto**: Ping cada 30 segundos o para evitar límites de pago

Render permite keep-alive razonable en el tier gratuito.

---

## 🎉 Resultado Final

Con cron-job.org configurado:

1. ✅ Tu servicio **NUNCA** se duerme
2. ✅ Todas las requests son **instantáneas**
3. ✅ No pagas nada extra
4. ✅ Mejor experiencia de usuario

**Tiempo total de configuración**: 5 minutos

---

## 🐛 Troubleshooting

### El cron job falla con error 503
- Es normal la primera vez si el servicio estaba dormido
- Espera 1-2 minutos y debería resolverse

### Los pings no aparecen en los logs de Render
- Verifica la URL en cron-job.org
- Asegúrate de que el servicio esté "Live" en Render

### El servicio sigue tardando después del keep-alive
- Espera 10-15 minutos después de configurar el cron
- Revisa que el intervalo sea 10 minutos (no mayor)

---

## 📖 Recursos

- Cron-Job.org: https://cron-job.org/
- UptimeRobot: https://uptimerobot.com/
- Documentación de Render: https://render.com/docs/free

---

**¿Configuraste el keep-alive?** ¡Tu backend ahora está siempre listo! 🚀
