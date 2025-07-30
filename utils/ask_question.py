from dotenv import load_dotenv
from google import genai
from google.genai import types
from utils.loader import load_data

load_dotenv()
client = genai.Client()

def answer_question_with_gemini(question: str) -> str:
    datasets = load_data()

    # Crear texto base con muestras de los datasets
    context = ""
    for level, df in datasets.items():
        try:
            sample = df.head(5000).to_string(index=False)
        except Exception:
            sample = "No se pudo cargar muestra para este nivel."
        context += f"\n--- {level.upper()} ---\n{sample}\n"

    prompt = f"""
Actúa como un experto en análisis de datos sociales. Tienes acceso a muestras de datos sobre seguridad alimentaria, nutrición y programas de alimentación escolar en Colombia. A continuación verás los datos en distintos niveles (regional, departamental, municipal).

Pregunta del usuario:
{question}

Datos:
{context}

Responde con base en los datos proporcionados, destacando patrones, variaciones o situaciones críticas si aplica. Usa un lenguaje técnico pero claro. Responde de manera concisa y directa, enfocándote en los hallazgos más relevantes.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_budget=0)
            )
        )
        return response.text.strip()
    except Exception as e:
        return f"Error al generar respuesta: {str(e)}"
