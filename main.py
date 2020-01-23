from selenium import webdriver
import re
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys



def init_browser():
    chromeDriver = "C:/Program Files/webdriver/chromedriver"
    options = Options()
    options.add_argument(' -- headless')
    options.add_argument(' -- disable-gpu')
    browser = webdriver.Chrome(chromeDriver)

    return browser

def yelp_iterator(browser):
    try:
       browser.get(f'https://www.yelp.com/') 
    except:
        print('site could not be found')
    
    time.sleep(5)
    
    # search = browser.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/label[1]/div[1]/span[2]/input[3]")
    zipCode = browser.find_element_by_name("find_desc")
    # search.sendKeys('wifi')
    # zipCode.click()
    print(zipCode.get_attribute('value'))
    zipCode.send_Keys('94555')


if __name__ == "__main__":
    browser = init_browser()
    yelp_iterator(browser)