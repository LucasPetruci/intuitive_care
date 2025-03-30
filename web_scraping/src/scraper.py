import os
import requests
import zipfile
import time
from selenium.webdriver.common.by import By
from urllib.parse import urljoin

class Scraper:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)
        return self.driver.title

    def get_pdf_links(self):
        pdf_links = []
        links = self.driver.find_elements(By.TAG_NAME, "a")
        for link in links:
            text = link.text.strip()
            href = link.get_attribute("href")
            if href and href.lower().endswith(".pdf") and ("Anexo I" in text or "Anexo II" in text):
                absolute_link = urljoin(self.driver.current_url, href)
                pdf_links.append(absolute_link)
        return pdf_links


    def download_pdfs(self, pdf_links, download_folder):
        os.makedirs(download_folder, exist_ok=True)
        for link in pdf_links:
            filename = link.split("/")[-1]
            filepath = os.path.join(download_folder, filename)
            response = requests.get(link)
            if response.status_code == 200:
                with open(filepath, "wb") as f:
                    f.write(response.content)
            else:
                print(f"Erro ao baixar o arquivo: {response.status_code}, {response.reason}")

    def compress_files(self, download_folder, zip_filename):
        with zipfile.ZipFile(zip_filename, "w") as zipf:
            for root, _, files in os.walk(download_folder):
                for file in files:
                    zipf.write(os.path.join(root, file), file)

    def wait_and_close(self, seconds):
        time.sleep(seconds)
        self.driver.close()
