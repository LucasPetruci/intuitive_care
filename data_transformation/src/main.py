from transformer import DataTransformer
import config

def main():

    transformer = DataTransformer(config.PDF_PATH, config.OUTPUT_CSV)

    transformer.convert_pdf_to_csv()
    abbreviations = transformer.extract_footer_abbreviations()
    transformer.replace_abbreviations_in_csv(abbreviations)
    transformer.csv_to_zip(config.ZIP_NAME)

if __name__ == "__main__":
    main()
