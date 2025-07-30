import textrazor
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
textrazor.api_key = os.getenv("TEXTRAZOR_API_KEY")

client = textrazor.TextRazor(extractors=["entities", "topics"])

def extract_keywords_from_text(text: str, max_keywords: int = 10):
    response = client.analyze(text)
    keywords = set()

    if response.ok:
        for entity in response.entities():
            if entity.confidence_score > 5:
                keywords.add(entity.id)
            if len(keywords) >= max_keywords:
                break
    return list(keywords)

def extract_relevant_text(data):

    df_all = pd.concat(data.values(), ignore_index=True).head(1000)

    # Posibles columnas que contienen contexto útil
    columnas_texto = [
        "indicador",
        "tipo_dato",
        "tipo_de_medida"
    ]

    columnas_existentes = [col for col in columnas_texto if col in df_all.columns]

    if not columnas_existentes:
        raise ValueError("No hay columnas textuales relevantes para analizar.")

    # Unir texto útil
    texto_concatenado = (
        df_all[columnas_existentes]
        .fillna("")
        .astype(str)
        .agg(" ".join, axis=1)
        .str.cat(sep=" ")
    )

    return texto_concatenado

