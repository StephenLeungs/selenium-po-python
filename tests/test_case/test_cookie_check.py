import time
from typing import Dict

import pytest

from selenium_po.operation.cookie_check_page_operation import CookieCheckPageOperation
from src.config.logging_config import get_logger
from src.selenium_po.utils.driver_utils import DriverUtils
from src.selenium_po.utils.excel_reader import ExcelReader


class TestCookieCheck:
    """
    登录态检查模块测试类

    调用登录态检查页操作类CookieCheckPageOperation的各个方法，以pytest参数化传入的测试数据作为参数，实现登录态检查功能
    """

    # 日志器
    logger = get_logger(
        log_name="TestCookieCheck",  # 使用类名作为日志器名称
        filename='./log/selenium-po.log',  # 所有类使用相同的日志文件
        level="INFO"  # 设置适当的日志级别
    )

    # 获取登录态检查页所需要的测试数据（用于@pytest.mark.parametrize装饰器进行参数化）
    reader = ExcelReader()
    cookie_check_test_data = reader.get_sheet_data_as_dict("LoginCookieCheckData")

    def setup_method(self) -> None:
        """
        setup_method特殊方法

        每个测试方法执行前都执行一次，调用浏览器管理工具类的方法打开浏览器并打开登录态检查页
        """
        self.driver = DriverUtils.get_driver()
        self.driver.get("http://127.0.0.1:8080/cookie_check")
        self.cookie_check_page_operation = CookieCheckPageOperation(self.driver)

    def teardown_method(self) -> None:
        """
        teardown_method特殊方法

        每个测试方法执行后都执行一次，调用浏览器管理工具类的方法关闭浏览器
        """
        DriverUtils.quit_driver()

    @pytest.mark.order(3)
    @pytest.mark.parametrize("cookie_check_data", cookie_check_test_data)
    def test_cookie_check(self, cookie_check_data: Dict[str, str]) -> None:
        """
        登录态检查 测试用例

        测试过程中的time.sleep()暂停仅供调试使用，可酌情删除

        Args:
            cookie_check_data: 通过@pytest.mark.parametrize装饰器参数化，读取Excel文件获得的存放登录态检查测试数据的字典
        """
        # 从字典中取出测试数据
        expected_result = cookie_check_data["expectedResult"]

        try:
            # 调用浏览器管理工具类的方法给当前浏览器实例添加cookie
            time.sleep(1)
            DriverUtils.add_cookie()

            # 点击登录态检查按钮
            time.sleep(1)
            self.cookie_check_page_operation.click_cookie_check_button()

            # 根据点击登录态检查按钮后，页面上出现的提示信息进行断言
            time.sleep(1)
            assert self.cookie_check_page_operation.get_cookie_check_result() == expected_result



        except Exception as e:
            self.logger.error(f"登录态检查测试用例异常: {e}")
            raise
