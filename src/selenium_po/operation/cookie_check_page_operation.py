from src.selenium_po.base.base_action import BaseAction
from src.selenium_po.page.cookie_check_page import CookieCheckPage


class CookieCheckPageOperation(BaseAction):
    def click_cookie_check_button(self):
        self.click(CookieCheckPage.CHECK_COOKIE_BUTTON)

    def get_cookie_check_result(self):
        return self.get_text(CookieCheckPage.CHECK_COOKIE_RESULT)
