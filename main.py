from fastapi import FastAPI
from utils.loader import load_data
from utils.summarizer import summarize_dataframe_map
from utils.keywords import extract_keywords_from_text
from utils.ask_question import answer_question_with_gemini
import pandas as pd
from fastapi import Query

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/summary")
def summary():
    datasets = load_data()
    resumen = summarize_dataframe_map(datasets)
    return {"summary": resumen}

@app.get("/keywords")
def get_keywords():
    try:
        # Cargar los datos desde el Excel (todas las hojas)
        datasets = load_data()
        
        # Combinar en un solo dataframe y limitar a 1000 filas
        df_all = pd.concat(datasets.values(), ignore_index=True).head(1000)
        
        # Convertir a texto plano para análisis
        text = df_all.astype(str).apply(lambda row: ' '.join(row), axis=1).str.cat(sep='\n')

        # Extraer palabras clave
        keywords = extract_keywords_from_text(text)
        return {"keywords": keywords}
    
    except Exception as e:
        return {"error": str(e)}
    

@app.get("/ask")
def ask(question: str = Query(..., description="Pregunta en lenguaje natural")):
    try:
        answer = answer_question_with_gemini(question)
        return {"question": question, "answer": answer}
    except Exception as e:
        return {"error": str(e)}