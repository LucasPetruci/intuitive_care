import tabula
import zipfile
import os
import pdfplumber

# Extract tables from PDF file and save it as CSV file
def convert_pdf_to_csv(pdf_path, output_csv):
    tabula.convert_into(
        input_path=pdf_path,
        output_path=output_csv,
        output_format="csv",
        pages="3-181",
    )
    
    print(f"Table extracted from {pdf_path} and saved as {output_csv}")
    
def csv_to_zip(csv_name, zip_name):
    with zipfile.ZipFile(zip_name, "w") as zipf:
        zipf.write(csv_name, os.path.basename(csv_name))
    
    print(f"{csv_name} saved as {zip_name}")
    
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
       
    
        
    
