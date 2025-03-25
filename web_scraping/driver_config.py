from selenium import webdriver

# Returns a Chrome driver
def get_driver():
    driver = webdriver.Chrome()
    return driver
