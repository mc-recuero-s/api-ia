import pandas as pd

def clean_and_normalize(df: pd.DataFrame) -> pd.DataFrame:
    # 1. Strip y lower en nombres de columnas
    df.columns = df.columns.str.strip().str.lower()

    # 2. Strip y lower en columnas tipo string
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].astype(str).str.strip().str.lower()

    # 3. Eliminar duplicados
    df = df.drop_duplicates()

    # 4. Reemplazar valores nulos en campos críticos (si aplica)
    if "valor" in df.columns:
        df["valor"] = pd.to_numeric(df["valor"], errors="coerce")

    # 5. Rellenar opcionalmente campos vacíos o marcar como "desconocido"
    for col in ["departamento", "municipio", "región", "indicador"]:
        if col in df.columns:
            df[col] = df[col].fillna("desconocido")

    return df


def load_data():
    data = {}

    try:
        df_dep = pd.read_excel("./data/Departamental.xlsx")
        df_dep["nivel"] = "departamental"
        df_dep = clean_and_normalize(df_dep)
        data["departamental"] = df_dep
    except Exception as e:
        print("Error cargando Departamental.xlsx:", e)

    try:
        df_mun = pd.read_excel("./data/Municipal.xlsx")
        df_mun["nivel"] = "municipal"
        df_mun = clean_and_normalize(df_mun)
        data["municipal"] = df_mun
    except Exception as e:
        print("Error cargando Municipal.xlsx:", e)

    try:
        df_reg = pd.read_excel("./data/Regional.xlsx")
        df_reg["nivel"] = "regional"
        df_reg = clean_and_normalize(df_reg)
        data["regional"] = df_reg
    except Exception as e:
        print("Error cargando Regional.xlsx:", e)

    return data
