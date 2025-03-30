from selenium import webdriver
import config

# Returns a driver
def get_driver():
    # for Chrome
    if config.WEB_DRIVER.lower() == "chrome":
        driver = webdriver.Chrome() 
    
    # for Firefox
    elif config.WEB_DRIVER.lower() == "firefox":
        driver = webdriver.Firefox()
   
    # for Edge
    elif config.WEB_DRIVER.lower() == "edge":
        driver = webdriver.Edge()
        
    else:
        raise ValueError(f"Webdriver '{config.WEB_DRIVER}' não suportado.")
    
    return driver
