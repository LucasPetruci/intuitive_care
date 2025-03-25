import time
import os
import requests
import zipfile
from selenium.webdriver.common.by import By
from urllib.parse import urljoin

def open_url(driver, url):
    driver.get(url)
    return driver.title

def get_pdf_link(driver):
    pdf_links = []
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        text = link.text.strip()
        href = link.get_attribute("href")
        if href and href.lower().endswith(".pdf") and ("Anexo I" in text or "Anexo II" in text):
            absolute_link = urljoin(driver.current_url, href)
            pdf_links.append(absolute_link)
    return pdf_links

def download_pdf(pdf_link, download_folder):
    for link in pdf_link:
        os.makedirs(download_folder, exist_ok=True)
        filename = link.split("/")[-1]
        filepath = os.path.join(download_folder, filename)
        
        response = requests.get(link)
        if response.status_code == 200:
            with open(filepath, "wb") as f:
                f.write(response.content)
        else:
            return f"Erro ao baixar o arquivo: {response.status_code, response.reason}"

def compress_file(download_folder, zip_filename):
    with zipfile.ZipFile(zip_filename, "w") as zipf:
        for root, _, files in os.walk(download_folder):
            for file in files:
                zipf.write(os.path.join(root, file), file)
    
def wait_and_close(driver, seconds):
    time.sleep(seconds)
    driver.close()