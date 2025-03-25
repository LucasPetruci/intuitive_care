from selenium import webdriver

# Returns a driver
def get_driver():
    # for Chrome
    driver = webdriver.Chrome()
    
    # for Firefox
    # driver = webdriver.Firefox()
    
    # for Edge
    # driver = webdriver.Edge()
    return driver
