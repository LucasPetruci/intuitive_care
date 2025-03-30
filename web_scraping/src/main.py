from driver_config import get_driver
from scraper import open_url, wait_and_close, get_pdf_link, download_pdf, compress_file
import config

def main():
    driver = get_driver()
    
    # Open the URL and extract the PDF links
    open_url(driver, config.BASE_URL)
    links_pdf = get_pdf_link(driver)
    
    # Close the browser after 5 seconds
    wait_and_close(driver, config.WAIT_SECONDS)
    
    # Download the PDF files and compress them into a ZIP file
    download_pdf(links_pdf, config.DOWLOAD_FOLDER)
    compress_file("downloads", config.ZIP_FILE_NAME)
    
if __name__ == "__main__":
    main()