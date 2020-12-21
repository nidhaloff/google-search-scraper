"""Main module."""
import requests
from bs4 import BeautifulSoup
from src.config import configs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def search(text: str):
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome('/usr/bin/chromedriver', options=None)
    url = configs["GOOGLE_URL"]
    driver.get(url)
    # driver.implicitly_wait(15)
    # accept_permissions_form = driver.find_element_by_id('introAgreeButton')
    # print("found: ", accept_permissions_form.get_attribute('rule'))
    # driver.implicitly_wait(15)
    # accept_permissions_form.click()

    search_box = driver.find_element_by_name('q')
    search_box.send_keys(text)
    search_box.send_keys(Keys.RETURN)

    links = driver.find_elements_by_css_selector('div.yuRUbf > a')
    for l in links:
        print(l.get_attribute('href'))
    return driver
    # driver.close()


if __name__ == '__main__':
    d = search("nidhal baccouri")
