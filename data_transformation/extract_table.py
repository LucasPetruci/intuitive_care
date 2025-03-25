import tabula
import zipfile
import os

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
        
    
