from src.selenium_po.base.base_action import BaseAction
from src.selenium_po.page.cookie_check_page import CookieCheckPage


class CookieCheckPageOperation(BaseAction):
    """
    登录态检查页面的具体操作类，继承自BaseAction。

    调用父类BaseAction提供的通用页面操作方法（如元素查找、输入等），
    封装了登录态检查流程相关的专属业务操作。
    """

    def click_cookie_check_button(self) -> None:
        """
        点击登录态检查按钮
        """
        self.click(CookieCheckPage.CHECK_COOKIE_BUTTON)

    def get_cookie_check_result(self) -> str:
        """
        获取登录态检查的结果信息

        Returns:
            str: 登录态检查的结果信息文本
        """
        return self.get_text(CookieCheckPage.CHECK_COOKIE_RESULT)
