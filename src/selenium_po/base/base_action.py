from typing import Tuple, Union

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    """
    基础页面操作类
    
    Attributes:
        driver (WebDriver): 浏览器实例
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        构造函数
        Args:
            driver: 浏览器实例
        """
        self.driver = driver

    def find_ele(self, ele: Tuple[str, str]) -> WebElement:
        """
        定位元素并添加显式等待

        Args:
            ele: 元素定位器元组，格式为(定位方式, 定位表达式)
                如: ("id", "username"), ("xpath", "//button[text()='Submit']")

        Returns:
            WebElement: 找到的页面元素
        """
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(lambda x: x.find_element(ele[0], ele[1]))
        return element

    def input(self, ele: Tuple[str, str], text: str) -> None:
        """
        在指定的元素中输入文本
        
        Args:
            ele: 元素定位器元组 
            text: 要输入的文本内容
        """
        self.find_ele(ele).send_keys(text)

    def clear_text(self, ele: Tuple[str, str]) -> None:
        """
        清除输入框中的文本
        
        Args:
            ele: 元素定位器元组
        """
        self.find_ele(ele).clear()

    def click(self, ele: Tuple[str, str]) -> None:
        """
        点击元素（左键单击）
        
        Args:
            ele: 元素定位器元组
        """
        self.find_ele(ele).click()

    def switch_to_frame(self, frame_reference: Union[str, int, WebElement]) -> None:
        """
        切换到指定的 frame/iframe。

        Args:
            frame_reference:用于定位 frame 的标识符，可以是 id/name(str), index(int) 或 WebElement 对象。
        """
        self.driver.switch_to.frame(frame_reference)

    def switch_to_default_content(self) -> None:
        """
        从frame切换回默认窗口内容
        """
        self.driver.switch_to.default_content()

    def get_text(self, ele: Tuple[str, str]) -> str:
        """
        获取元素文本

        Args:
            ele: 元素定位器元组

        Returns:
            str: 获取到的文本
        """
        msg = self.find_ele(ele)
        return msg.text

    def select_check(self, ele: Tuple[str, str]) -> None:
        """
        勾选操作

        Args:
            ele: 元素定位器元组
        """
        element = self.find_ele(ele)
        if not (element.is_selected()):
            element.click()
