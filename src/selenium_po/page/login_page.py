from abc import ABC
from typing import Final

from selenium.webdriver.common.by import By


class LoginPage(ABC):
    """登录页 页面元素定位器类，使用抽象基类ABC防止类被实例化"""

    # 页面元素定位器（添加常量标识": Final"）
    REGISTER_RADIO_BUTTON: Final = (By.CSS_SELECTOR, "#registerRadio")
    LOGIN_RADIO_BUTTON: Final = (By.CSS_SELECTOR, "#loginRadio")
    USERNAME: Final = (By.CSS_SELECTOR, "#username")
    PASSWORD: Final = (By.CSS_SELECTOR, "#password")
    CONFIRM_PASSWORD: Final = (By.CSS_SELECTOR, "#confirmPassword")
    CONFIRM_BUTTON: Final = (By.CSS_SELECTOR, "#submitBtn")
    MESSAGE: Final = (By.CSS_SELECTOR, "#message")

    def __init__(self):
        raise TypeError("LoginPage is a utility class and cannot be instantiated")
