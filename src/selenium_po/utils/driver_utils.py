import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.driver_cache import DriverCacheManager


class DriverUtils:
    """
    浏览器管理工具类

    用于提供浏览器管理的各个工具方法（比如打开、关闭浏览器、cookie管理等）
    """
    # 浏览器和存放cookie的字典
    driver = None
    save_cookie = None

    @classmethod
    def get_driver(cls) -> WebDriver:
        """
        打开浏览器

        通过Selenium提供的webdriver.Chrome()方法添加浏览器设置并打开浏览器

        Returns:
            WebDriver: Chrome浏览器实例
        """

        # os.environ['WDM_DOWNLOAD_BASE_URL'] = "https://registry.npmmirror.com/binary.html?path=chrome-for-testing/"

        # 浏览器设置
        options = Options()
        options.add_argument("--start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])

        # 设置webdriver-manager下载驱动的镜像源
        service = ChromeService(ChromeDriverManager(
            url="https://registry.npmmirror.com/binary.html?path=chrome-for-testing/",
            cache_manager=DriverCacheManager(valid_range=180)).install())

        # 获取Chrome浏览器实例
        cls.driver = webdriver.Chrome(service=service, options=options)

        return cls.driver

    @classmethod
    def quit_driver(cls) -> None:
        """
        关闭浏览器
        """
        time.sleep(2)
        cls.driver.quit()

    @classmethod
    def get_all_cookies(cls) -> None:
        """
        获取cookie

        获取当前浏览器实例的所有cookie，并添加到存放cookie的字典中
        """
        cls.save_cookie = cls.driver.get_cookies()

    @classmethod
    def add_cookie(cls) -> None:
        """
        添加cookie

        遍历存放cookie的字典，并把所有cookie添加到当前的浏览器实例中
        """
        cls.driver.delete_all_cookies()
        for cookie in cls.save_cookie:
            cls.driver.add_cookie({'name': cookie['name'], 'value': cookie['value']})
        cls.driver.refresh()
