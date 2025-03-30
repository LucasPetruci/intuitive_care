from driver_config import get_driver
from scraper import open_url, wait_and_close, get_pdf_link, download_pdf, compress_file

def main():
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    driver = get_driver()
    
    # Open the URL and extract the PDF links
    open_url(driver, url)
    links_pdf = get_pdf_link(driver)
    
    # Close the browser after 5 seconds
    wait_and_close(driver, 5)
    
    # Download the PDF files and compress them into a ZIP file
    download_pdf(links_pdf, "downloads")
    compress_file("downloads", "downloads.zip")
    
if __name__ == "__main__":
    main()