# 🥦 NutriData Insights API - Análisis de Datos sobre Alimentación y Nutrición en Colombia

Esta es una API desarrollada en FastAPI que permite analizar datos sobre seguridad alimentaria, nutrición y programas de alimentación escolar en Colombia.

## 🧠 ¿Qué hace esta API?

La API ofrece funcionalidades para:

- ✅ Resumir los datos con un lenguaje claro y conciso usando Gemini.
- 🔑 Extraer palabras clave que ayuden a entender los temas principales del dataset usando TextRazor.
- ❓ Responder preguntas formuladas en lenguaje natural usando Gemini, como:  
  *“¿Qué tendencia se observa en el acceso a programas de alimentación escolar?”*
- 🩺 Verificar que la API esté activa con `/ping`.

## 📥 Carga y Transformación de Datos (`loader.py`)

Antes de trabajar con los datos, se realiza un paso fundamental: **la carga y transformación** de los archivos Excel. Este paso incluye:

- Lectura de los archivos `.xlsx`.
- Selección de columnas relevantes.
- Eliminación de filas vacías o incompletas.
- Conversión de los datos en un texto estructurado, amigable para los modelos de lenguaje.

👉 **¿Por qué es importante transformar los datos?**  
Los modelos como Gemini funcionan mejor cuando se les da información clara, limpia y coherente. Si los datos tienen errores, espacios vacíos, valores faltantes o formatos inconsistentes, las respuestas pueden ser incorrectas o poco útiles.

## 🧾 Prompts Iniciales

Para guiar correctamente al modelo de lenguaje, configuramos **prompts iniciales** en los módulos `summarizer.py`, `keywords.py` y `ask_question.py`. Estos prompts:

- Le indican a Gemini cuál es su rol (por ejemplo, *"Eres un analista de datos especializado en seguridad alimentaria en Colombia..."*).
- Le proporcionan el contexto necesario sobre el contenido del dataset.
- Lo orientan para que genere resúmenes o respuestas en lenguaje claro, técnico pero accesible.

👉 **¿Por qué son clave los prompts iniciales?**  
Un buen prompt es la base para obtener resultados útiles. Si no se define bien lo que se espera del modelo, este puede dar respuestas demasiado genéricas o desviadas del contexto colombiano.

## 📁 Estructura del Proyecto

.
├── main.py
├── utils/
│ ├── loader.py
│ ├── summarizer.py
│ ├── keywords.py
│ └── ask_question.py
├── requirements.txt
├── .env
└── README.md


## 🚀 Requisitos

- Python 3.10+
- Archivos Excel con los datos a cargar (`.xlsx`). En este caso el repositorio ya cuenta con unos archivos almacenados en la carpeta data.
- Cuenta y clave API de Google Gemini
- Cuenta y clave API de Text Razor

## 🛠️ Instalación Local

1. **Clona el repositorio:**

```bash
git clone https://github.com/mc-recuero-s/api-ia.git
cd api-ia
```

2. **Crea un entorno virtual, activarlo e instalar dependencias:**

```bash
pip install virtualenv
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
pip install -r requirements.txt
```

3. **Configura tus variables de entorno:**

Crea un archivo .env con estas variables:
```bash
GEMINI_API_KEY=tu_clave_api_de_gemini
TEXTRAZOR_API_KEY=tu_clave_api_de_textrazor
```

4. **Corre la app:**
```bash
uvicorn main:app --reload
```

5. **Accede a la documentación para usar los endpoints:**

```bash
http://localhost:8000/docs
```