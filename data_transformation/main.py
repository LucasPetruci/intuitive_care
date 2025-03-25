from extract_table import convert_pdf_to_csv, csv_to_zip, extract_footer, replace_abbreviations_in_csv

def main():
    pdf_path = "../web_scraping/downloads/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
    output_csv = "rol_de_procedimentos.csv" 
    name_zip = "Teste_lucas_petruci.zip"
    
    convert_pdf_to_csv(pdf_path, output_csv)
    csv_to_zip(output_csv, name_zip)
    abbreviations = extract_footer(pdf_path)
    replace_abbreviations_in_csv(output_csv, abbreviations)
    
if __name__ == "__main__":
    main()