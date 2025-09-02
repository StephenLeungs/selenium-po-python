from src.selenium_po.base.base_action import BaseAction
from src.selenium_po.page.login_page import LoginPage


class LoginPageOperation(BaseAction):
    """
    登录页面的具体操作类，继承自BaseAction。

    调用父类BaseAction提供的通用页面操作方法（如元素查找、输入等），
    封装了登录流程相关的专属业务操作。
    """

    def click_register_radio_button(self) -> None:
        """
        点击注册单选按钮
        """
        self.click(LoginPage.REGISTER_RADIO_BUTTON)

    def click_login_radio_button(self) -> None:
        """
        点击登录单选按钮
        """
        self.click(LoginPage.LOGIN_RADIO_BUTTON)

    def input_username(self, username: str) -> None:
        """
        输入账号

        Args:
            username: 账号
        """
        self.input(LoginPage.USERNAME, username)

    def input_password(self, password: str) -> None:
        """
        输入密码

        Args:
            password: 密码
        """
        self.input(LoginPage.PASSWORD, password)

    def input_confirm_password(self, confirm_password: str) -> None:
        """
        输入确认密码

        Args:
            confirm_password: 确认密码
        """
        self.input(LoginPage.CONFIRM_PASSWORD, confirm_password)

    def click_confirm_button(self) -> None:
        """
        点击确认按钮
        """
        self.click(LoginPage.CONFIRM_BUTTON)

    def get_message(self) -> str:
        """
        获取注册或登录操作后的提示信息

        Returns:
            str: 注册或登录操作后的提示信息文本
        """
        return self.get_text(LoginPage.MESSAGE)

    def clear_username(self) -> None:
        """
        清空账号输入框的内容
        """
        self.clear_text(LoginPage.USERNAME)

    def clear_password(self) -> None:
        """
        清空密码输入框的内容
        """
        self.clear_text(LoginPage.PASSWORD)
