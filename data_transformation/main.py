from extract_table import extract_table_from_pdf, save_table_to_csv
import os

def main():
    pdf_path = "../web_scraping/downloads/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
    output_csv = "rol_de_procedimentos.csv"
    
    tables = extract_table_from_pdf(pdf_path)
    save_table_to_csv(tables, output_csv)
    
if __name__ == "__main__":
    main()