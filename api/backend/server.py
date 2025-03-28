from fastapi import FastAPI, HTTPException
from handle_csv import HandleCSV

app = FastAPI()
path = "../../data_base/data/operadoras_ativas/Relatorio_cadop.csv"

csv_handler = HandleCSV(path)
    
@app.get("/search")
def search_endpoint(search: str, column: str):
    try:
        result =  csv_handler.search(
            search_value=search,
            column_search=column,
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
   