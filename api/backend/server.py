from fastapi import FastAPI
import pandas as pd
from read_csv import read_csv

app = FastAPI()
path = "../../data_base/data/operadoras_ativas/Relatorio_cadop.csv"

@app.get("/")
def read_root():
    data = read_csv(path)
    return data.to_dict(orient='records')
   