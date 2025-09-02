from abc import ABC
from typing import Final

from selenium.webdriver.common.by import By


class LoginPage(ABC):
    """
    登录页 页面元素定位器类，通过继承抽象基类ABC，防止类被实例化
    """

    # 登录页上的元素的定位器元组（添加常量标识": Final"）
    # 注册单选按钮
    REGISTER_RADIO_BUTTON: Final = (By.CSS_SELECTOR, "#registerRadio")

    # 登录单选按钮
    LOGIN_RADIO_BUTTON: Final = (By.CSS_SELECTOR, "#loginRadio")

    # 账号输入框
    USERNAME: Final = (By.CSS_SELECTOR, "#username")

    # 密码输入框
    PASSWORD: Final = (By.CSS_SELECTOR, "#password")

    # 确认密码输入框
    CONFIRM_PASSWORD: Final = (By.CSS_SELECTOR, "#confirmPassword")

    # 确定按钮
    CONFIRM_BUTTON: Final = (By.CSS_SELECTOR, "#submitBtn")

    # 注册/登录操作后的提示信息文本
    MESSAGE: Final = (By.CSS_SELECTOR, "#message")

    def __init__(self):
        """
        构造函数
        使用抛出错误的方式，代替实例化操作，防止类被实例化
        """
        raise TypeError("LoginPage is a utility class and cannot be instantiated")
