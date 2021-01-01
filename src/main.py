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

    def search(self, text: str, detailed=False):
        results = {}
        self.driver.get(self.url)
        search_box = self.driver.find_element_by_name('q')
        search_box.send_keys(text)
        search_box.send_keys(Keys.RETURN)
        tabs = self.get_tabs()
        d = self.map_tabs_to_names(tabs)

        links = self.driver.find_elements_by_css_selector('div.yuRUbf > a')
        results['links'] = [link.get_attribute('href') for link in links]
        return results if not detailed else self.advanced_search(tabs_map=d, results=results)

    def advanced_search(self, tabs_map: dict, results: dict):
        for key, val in tabs_map.items():
            self.driver.get(val)
            if key == 'news':
                links = self.driver.find_elements_by_css_selector('div.dbsr > a')
                results[key] = [link.get_attribute('href') for link in links]
            elif key == 'images':
                # # div.bRMDJf.islir > img
                links = self.driver.find_elements_by_css_selector('a.wXeWr.islib.nfEiy.mM5pbd')
                results[key] = [link.get_attribute('href') for link in links]
            else:
                links = self.driver.find_elements_by_css_selector('div.yuRUbf > a')
                results[key] = [link.get_attribute('href') for link in links]

        return results

    def get_tabs(self):
        tabs = self.driver.find_elements_by_css_selector('a.hide-focus-ring')
        return [tab.get_attribute('href') for tab in tabs if tab.get_attribute('href')]


if __name__ == '__main__':
    _, res = GoogleScraper().search("donald trump", detailed=True)
    for k, v in res.items():
        print(f"{k} results: "
              f"{v}")
