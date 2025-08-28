from src.selenium_po.base.base_action import BaseAction
from src.selenium_po.page.login_page import LoginPage


class LoginPageOperation(BaseAction):
    def click_register_radio_button(self):
        self.click(LoginPage.REGISTER_RADIO_BUTTON)

    def click_login_radio_button(self):
        self.click(LoginPage.LOGIN_RADIO_BUTTON)

    def input_username(self, username):
        self.input(LoginPage.USERNAME, username)

    def input_password(self, password):
        self.input(LoginPage.PASSWORD, password)

    def input_confirm_password(self, confirm_password):
        self.input(LoginPage.CONFIRM_PASSWORD, confirm_password)

    def click_confirm_button(self):
        self.click(LoginPage.CONFIRM_BUTTON)

    def get_message(self):
        return self.get_text(LoginPage.MESSAGE)

    def clear_username(self):
        self.clear_text(LoginPage.USERNAME)

    def clear_password(self):
        self.clear_text(LoginPage.PASSWORD)
