"""Main module."""

from src.config import configs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class GoogleScraper(object):
    def __init__(self, chrome_driver_path: str = '/usr/bin/chromedriver'):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.url = configs["GOOGLE_URL"]
        self.driver = webdriver.Chrome(chrome_driver_path, options=None)  # options

    def map_tabs_to_names(self, tabs: list):
        d = {}
        for tab in tabs:
            if tab.find('nws') > -1:
                d['news'] = tab
            elif tab.find('isch') > -1:
                d['images'] = tab
            elif tab.find('vid') > -1:
                d['videos'] = tab
        return d

    def search(self, text: str, advanced_search=False):
        results = {}
        self.driver.get(self.url)
        search_box = self.driver.find_element_by_name('q')
        search_box.send_keys(text)
        search_box.send_keys(Keys.RETURN)
        tabs = self.get_tabs()
        d = self.map_tabs_to_names(tabs)

        links = self.driver.find_elements_by_css_selector('div.yuRUbf > a')
        results['links'] = [link.get_attribute('href') for link in links]
        if not advanced_search:
            return results

        # search further images and videos results:
        for k, v in d.items():
            self.driver.get(v)
            links = self.driver.find_elements_by_css_selector('div.yuRUbf > a')
            results[k] = [link.get_attribute('href') for link in links]

        return self.driver, results
        # driver.close()

    def get_tabs(self):
        tabs = self.driver.find_elements_by_css_selector('a.hide-focus-ring')
        return [tab.get_attribute('href') for tab in tabs if tab.get_attribute('href')]


if __name__ == '__main__':
    _, res = GoogleScraper().search("donald trump", advanced_search=True)
    for k, v in res.items():
        print(f"{k} results: "
              f"{v}")
