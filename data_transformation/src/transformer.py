import tabula
import zipfile
import os
import pdfplumber
import pandas as pd

class DataTransformer:
    def __init__(self, pdf_path, csv_path):
        self.pdf_path = pdf_path
        self.csv_path = csv_path

    def convert_pdf_to_csv(self, pages="3-181"):
        tabula.convert_into(
            input_path=self.pdf_path,
            output_path=self.csv_path,
            output_format="csv",
            pages=pages,
        )

    def csv_to_zip(self, zip_name):
        with zipfile.ZipFile(zip_name, "w") as zipf:
            zipf.write(self.csv_path, os.path.basename(self.csv_path))

    def extract_footer_abbreviations(self):
        with pdfplumber.open(self.pdf_path) as pdf:
            last_page = pdf.pages[-1]
            footer_text = last_page.extract_text()

            abbreviations = {}
            if "Legenda" in footer_text:
                legend_text = footer_text.split("Legenda:")[1]

                od_description = legend_text.split("OD:")[1].split("HSO")[0].strip()
                amb_description = legend_text.split("AMB:")[1].split("REF")[0].strip()

                abbreviations["OD"] = od_description
                abbreviations["AMB"] = amb_description

            return abbreviations

    def replace_abbreviations_in_csv(self, abbreviations):
        df = pd.read_csv(self.csv_path)

        for col in df.columns:
            for abbreviation, description in abbreviations.items():
                if df[col].astype(str).str.contains(abbreviation).any():
                    df[col] = df[col].str.replace(abbreviation, description, regex=False)

        df.to_csv(self.csv_path, index=False)
        print(f"Abbreviations replaced in {self.csv_path}")
