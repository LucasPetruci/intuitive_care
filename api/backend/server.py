from fastapi import FastAPI, HTTPException
import pandas as pd
from handle_csv import read_csv, search_in_csv

app = FastAPI()
path = "../../data_base/data/operadoras_ativas/Relatorio_cadop.csv"
    
@app.get("/search")
def search_endpoint(search: str, column: str):
    try:
        return search_in_csv(
            search_value=search,
            column_search=column,
            path=path,
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
   