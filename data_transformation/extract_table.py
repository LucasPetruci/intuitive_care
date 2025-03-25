import pandas as pd
import tabula

# Extract tables from PDF file
def extract_table_from_pdf(pdf_path):
    print(f"Extraindo tabelas do PDF: {pdf_path}")
    tables = tabula.read_pdf(pdf_path, pages="3-181", multiple_tables=True)
    if not tables:
        raise ValueError("Nenhuma tabela encontrada no PDF.")
    print(f"{len(tables)} tabelas extraídas.")
    return tables

def save_table_to_csv(tables, output_csv):
    if not tables:
        raise ValueError("Nenhuma tabela encontrada.")
    
    df = pd.concat(tables, ignore_index=True)
    df.to_csv(output_csv, index=False)
    print(f"Dados extraídos e salvos em: {output_csv}")
    return df