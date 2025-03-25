import tabula
import zipfile
import os
import pdfplumber
import pandas as pd

# Extract tables from PDF file and save it as CSV file
def convert_pdf_to_csv(pdf_path, output_csv):
    tabula.convert_into(
        input_path=pdf_path,
        output_path=output_csv,
        output_format="csv",
        pages="3-181",
    )
    
   
def csv_to_zip(csv_name, zip_name):
    with zipfile.ZipFile(zip_name, "w") as zipf:
        zipf.write(csv_name, os.path.basename(csv_name))    


def extract_footer(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        last_page = pdf.pages[-1]  
        footer_text = last_page.extract_text() 
        
        if "Legenda" in footer_text:
            # All text after "Legenda:"
            legend_text = footer_text.split("Legenda:")[1]
            
            abbreviations = {}
            
            # All text after "OD:" and before "HSO"
            od_description = legend_text.split("OD:")[1].split("HSO")[0].strip() 
            
            # All text after "AMB:" and before "REF"
            amb_description = legend_text.split("AMB:")[1].split("REF")[0].strip()
            
            abbreviations["OD"] = od_description
            abbreviations["AMB"] = amb_description
            
            print(abbreviations)
            return abbreviations
        

# Loop through all columns in the CSV file and replace abbreviations with their descriptions        
def replace_abbreviations_in_csv(csv_path, abbreviations):
    df = pd.read_csv(csv_path)

    for col in df.columns:
        for abbreviation, description in abbreviations.items():
            if df[col].astype(str).str.contains(abbreviation).any():
                df[col] = df[col].str.replace(abbreviation, description, regex=False)

    df.to_csv(csv_path, index=False)
    print(f"Abbreviations replaced in {csv_path}")