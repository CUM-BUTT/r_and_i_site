from unittest import TestCase

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
#import ddg3
import yandex_search

class GetHrefsFromSearch:
    search_url = 'https://duckduckgo.com/'

    def setUp(self):
        driver_path = 'yandexdriver.exe'  # path to YandexDriver
        options = webdriver.ChromeOptions()
        options.headless = False  # True
        self.driver = webdriver.Chrome(driver_path, options=options)

    def tearDown(self):
        self.driver.close()

    def OpenSearch(self, query):
        # arrange
        self.driver.get(self.search_url + '/' + query)

    def GetItemHrefs(self):
        self.driver.find_elements(by=By.CLASS_NAME, value='result-title-a',)

    def MoreResults(self):
        more_results_buton = self.driver.find_elements(by=By.CLASS_NAME, value='result--more__btn')
        while len(more_results_buton) > 0:
            more_results_buton[0].click()

        print(more_results_buton)

    def test_SearchExist(self):
        # arrange
        self.driver.get(self.urls['search'])

        # act
        search_field = self.driver.find_element_by_xpath(self.xpaths['search field'])

        # assert
        self.assertIsNotNone(search_field)

    def test_FindKojuhovInPeople(self):
        # arrange
        self.driver.get(self.urls['search'])

        # act
        search = self.driver.find_element_by_xpath(self.xpaths['search field'])
        search.send_keys('Кожухов')
        search.send_keys(Keys.ENTER)

        self.driver.find_element_by_xpath(self.xpaths['search people']).click()

        kojuhov = self.driver.find_element_by_xpath(self.xpaths['Kojuhov']).text

        # assert
        self.assertIn('Кожухов', kojuhov)

    def test_FindAWdlhiG(self):
        # arrange
        self.driver.get(self.urls['search'])

        # act
        search = self.driver.find_element_by_xpath(self.xpaths['search field'])
        search.send_keys('AWdlhiG')
        search.send_keys(Keys.ENTER)

        zero = int(self.driver.find_element_by_xpath(self.xpaths['searched count']).get_attribute('data-count'))

        # assert
        self.assertEquals(zero, 0)

    def test_FindKojuhovButWrongKeyboardLayout(self):
        # arrange
        self.driver.get(self.urls['search'])

        # act
        search = self.driver.find_element_by_xpath(self.xpaths['search field'])
        search.send_keys('Rj;e[jd')
        search.send_keys(Keys.ENTER)

        result_count = int(self.driver.find_element_by_xpath(self.xpaths['searched count']).get_attribute('data-count'))

        # assert
        self.assertGreater(result_count, 0)


    def test_FindKojuhovResultsItems(self):
        # arrange
        self.driver.get(self.urls['search'])

        # act
        search = self.driver.find_element_by_xpath(self.xpaths['search field'])
        search.send_keys('Кожухов')
        search.send_keys(Keys.ENTER)

        self.driver.find_element_by_xpath(self.xpaths['search people']).click()

        items = self.driver.find_elements_by_css_selector('body > main > div > div.result-list > div > div > div')

        # assert
        [self.assertIsNotNone(item.text) for item in items]

if __name__ == '__main__':
    parser = GetHrefsFromSearch()
    parser.setUp()
    parser.OpenSearch('huy')
    parser.MoreResults()