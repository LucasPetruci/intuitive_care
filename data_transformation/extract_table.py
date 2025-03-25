import tabula

# Extract tables from PDF file and save it as CSV file
def convert_pdf_to_csv(pdf_path, output_csv):
    tabula.convert_into(
        input_path=pdf_path,
        output_path=output_csv,
        output_format="csv",
        pages="3-181",
    )
    
    print(f"Table extracted from {pdf_path} and saved as {output_csv}")
    
