from fastapi import FastAPI, HTTPException
import pandas as pd
from handle_csv import read_csv

app = FastAPI()
path = "../../data_base/data/operadoras_ativas/Relatorio_cadop.csv"

@app.get("/")
def read_root():
    try:
        data = read_csv(path)
        return data.to_dict(orient='records')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
   