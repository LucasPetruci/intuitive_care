from extract_table import convert_pdf_to_csv

def main():
    pdf_path = "../web_scraping/downloads/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
    output_csv = "rol_de_procedimentos.csv" 
    
    convert_pdf_to_csv(pdf_path, output_csv)
    
if __name__ == "__main__":
    main()