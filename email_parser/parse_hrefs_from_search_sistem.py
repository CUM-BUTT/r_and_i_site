from unittest import TestCase
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

class GetHrefsFromSearch:
    search_url = ''

    def setUp(self):
        driver_path = 'yandexdriver.exe'  # path to YandexDriver
        options = webdriver.ChromeOptions()
        options.headless = not False  # True
        self.driver = webdriver.Chrome(driver_path, options=options)

        self.urls = {
            'search': 'https://miet.ru/search',
            'login': 'https://account.miet.ru/login?backurl=https%3A%2F%2Fmiet.ru%2Fsearch',
            'profile': 'https://account.miet.ru/profile',

        }
        self.xpaths = {
            'login': '//*[@id="inputLogin"]',
            'password': '//*[@id="inputPassword"]',
            'enter button': '/html/body/div/div/div[2]/form/div/button',
            'common data': '/html/body/main/div[2]/div[2]/div/div/form/fieldset/legend[1]',
            'search button': '/html/body/div/div[2]/a',
            'search field': '/html/body/main/div/div[1]/form/input',
            'search people': '/html/body/main/div/div[1]/div/a[2]',
            'Kojuhov': '/html/body/main/div/div[2]/div/div/div[1]/a',
            'searched count': '/html/body/main/div/div[1]/div/a[1]',
        }

    def tearDown(self):
        self.driver.close()

    def test_Login(self):
        # arrange
        self.driver.get(self.urls['login'])

        # act
        self.driver.find_element_by_xpath(self.xpaths['login']).send_keys('8171972')
        self.driver.find_element_by_xpath(self.xpaths['password']).send_keys('1809-1832i')
        self.driver.find_element_by_xpath(self.xpaths['enter button']).click()

        # assert
        self.driver.get(self.urls['profile'])
        common_data = self.driver.find_element_by_xpath(self.xpaths['common data']).text
        self.assertEquals('Общие данные', common_data)

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