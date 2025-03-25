import time
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
        

def wait_and_close(driver, seconds):
    time.sleep(seconds)
    driver.close()