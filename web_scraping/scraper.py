import time
import os
import requests
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
            print(f"Found PDF: {absolute_link}")
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
            print(f"Arquivo salvo em: {filepath}")
        else:
            print(f"Falha ao baixar: {pdf_link}")

def wait_and_close(driver, seconds):
    time.sleep(seconds)
    driver.close()