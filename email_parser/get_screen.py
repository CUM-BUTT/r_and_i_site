from pathlib import Path
from unittest import TestCase
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
#import ddg3
import yandex_search

class ScreenParser:
    def SetUp(self):
        driver_path = 'yandexdriver.exe'  # path to YandexDriver
        options = webdriver.ChromeOptions()
        mobile_emulation = {
            "deviceMetrics": { "width": 429, "height": 883, "pixelRatio": 3.0 },
            "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        options.headless = not False  # True
        self.driver = webdriver.Chrome(driver_path, options=options)

    def GetScreen(self, url, out_path: Path):
        self.driver.get(url)
        self.driver.save_screenshot(out_path)


if __name__ == '__main__':


    url = 'https://yandex.ru/'

    parser = ScreenParser()
    parser.SetUp()
    parser.ScreenParser(url, 'test')
