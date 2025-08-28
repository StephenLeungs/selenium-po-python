from abc import ABC
from typing import Final

from selenium.webdriver.common.by import By


class CookieCheckPage(ABC):
    """登录态检查页 页面元素定位器类，使用抽象基类ABC防止类被实例化"""

    # 页面元素定位器（添加常量标识": Final"）
    CHECK_COOKIE_PAGE_TEXT: Final = (By.CSS_SELECTOR, "body > div > h2")
    CHECK_COOKIE_BUTTON: Final = (By.CSS_SELECTOR, "#checkBtn")
    CHECK_COOKIE_RESULT: Final = (By.CSS_SELECTOR, "#result")

    def __init__(self):
        raise TypeError("CookieCheckPage is a utility class and cannot be instantiated")
