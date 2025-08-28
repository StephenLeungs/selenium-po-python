import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.driver_cache import DriverCacheManager


class DriverUtils:
    driver = None
    save_cookie = None

    @classmethod
    def get_driver(cls):
        # os.environ['WDM_DOWNLOAD_BASE_URL'] = "https://registry.npmmirror.com/binary.html?path=chrome-for-testing/"

        options = Options()
        options.add_argument("--start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])

        service = ChromeService(ChromeDriverManager(
            url="https://registry.npmmirror.com/binary.html?path=chrome-for-testing/",
            cache_manager=DriverCacheManager(valid_range=180)).install())
        cls.driver = webdriver.Chrome(service=service, options=options)

        return cls.driver

    @classmethod
    def quit_driver(cls):
        time.sleep(2)
        cls.driver.quit()

    @classmethod
    def get_all_cookies(cls):
        cls.save_cookie = cls.driver.get_cookies()

    @classmethod
    def add_cookie(cls):
        cls.driver.delete_all_cookies()
        for cookie in cls.save_cookie:
            cls.driver.add_cookie({'name': cookie['name'], 'value': cookie['value']})
        cls.driver.refresh()
