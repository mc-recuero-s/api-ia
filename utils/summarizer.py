import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()

def summarize_dataframe_map(datasets: dict) -> str:
    combined_text = ""

    for level, df in datasets.items():
        # Escoge una muestra representativa
        try:
            sample = df.head(10).to_string(index=False)
        except Exception:
            sample = "No se pudo cargar muestra para este nivel."

        section_title = level.capitalize()
        combined_text += f"\n=== {section_title} ===\n{sample}\n"

    # Prompt para Gemini
    prompt = f"""
Actúa como un analista de datos. A continuación verás una muestra de datos sobre alimentación y nutrición en Colombia en distintos niveles: regional, departamental y municipal.

Para cada nivel, identifica hallazgos importantes, patrones o situaciones críticas. Resume esta información en lenguaje claro y técnico. Finalmente se debe generar un resumen general con insights principales derivados de los datos.

{combined_text}

Resumen:
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
        return f"Error al generar resumen: {str(e)}"
