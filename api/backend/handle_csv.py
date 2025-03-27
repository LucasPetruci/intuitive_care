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