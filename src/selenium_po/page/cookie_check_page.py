from abc import ABC
from typing import Final

from selenium.webdriver.common.by import By


class CookieCheckPage(ABC):
    """
    登录态检查页 页面元素定位器类，通过继承抽象基类ABC，防止类被实例化
    """

    # 登录态检查页上的元素的定位器元组（添加常量标识": Final"）
    # 检查操作框的标题文本
    CHECK_COOKIE_PAGE_TEXT: Final = (By.CSS_SELECTOR, "body > div > h2")

    # 检查登录态按钮
    CHECK_COOKIE_BUTTON: Final = (By.CSS_SELECTOR, "#checkBtn")

    # 登录态检查结果
    CHECK_COOKIE_RESULT: Final = (By.CSS_SELECTOR, "#result")

    def __init__(self) -> None:
        """
        构造函数

        使用抛出错误的方式，代替实例化操作，防止类被实例化
        """
        raise TypeError("CookieCheckPage is a utility class and cannot be instantiated")
