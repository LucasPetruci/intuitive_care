from driver_config import get_driver
from scraper import Scraper
import config

def main():
    driver = get_driver()
    scraper = Scraper(driver)
    
    # Open the URL and extract the PDF links
    scraper.open_url(config.BASE_URL)
    links_pdf = scraper.get_pdf_links()
    
    # Close the browser after 5 seconds
    scraper.wait_and_close(config.WAIT_SECONDS)
    
    # Download the PDF files and compress them into a ZIP file
    scraper.download_pdfs(links_pdf, config.DOWLOAD_FOLDER)
    scraper.compress_files(config.DOWLOAD_FOLDER, config.ZIP_FILE_NAME)
    
if __name__ == "__main__":
    main()