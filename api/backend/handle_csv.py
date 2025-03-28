import pandas as pd
import numpy as np

def read_csv(path):
    try:
        df = pd.read_csv(
            path, 
            sep=';', 
            encoding='utf-8',
            dtype=str
        )
        df = df.replace([np.inf, -np.inf], np.nan)
        df = df.where(pd.notnull(df), None)
    
        return df
    except Exception as e:
        raise Exception(f"Failed to read CSV: {str(e)}")
    
def search_in_csv(search_value: str, column_search: str, path: str):
    try:
        df = read_csv(path)
        
        # Check if column_search is empyt
        if not column_search.strip():
            search_value = search_value.lower()
            mask = df.astype(str).apply(lambda col: col.str.lower().str.contains(search_value, na=False))
            results = df[mask.any(axis=1)]
            return results.to_dict(orient='records')
               
        # Remove spaces and underscores and convert to lowercase
        column_search = column_search.strip().lower().replace(" ", "").replace("_", "")
        df_columns_lower = [col.strip().lower().replace(" ", "").replace("_", "") 
                          for col in df.columns]
        matching_columns = [real_col for real_col, lower_col in zip(df.columns, df_columns_lower)
                          if lower_col == column_search]
        
        if not matching_columns:
            available_columns = ", ".join(df.columns)
            raise Exception(f"Coluna '{column_search}' não encontrada. Colunas disponíveis: {available_columns}")
        
        real_column_name = matching_columns[0]

        search_value = search_value.lower()
        results = df[
            df[real_column_name].astype(str).str.lower().str.contains(search_value, na=False)
        ]
        
        return results.to_dict(orient='records')

    except Exception as e:
        raise Exception(f"Failed to search in CSV: {str(e)}")