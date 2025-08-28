import time

import pytest

from selenium_po.operation.cookie_check_page_operation import CookieCheckPageOperation
from src.config.logging_config import get_logger
from src.selenium_po.utils.driver_utils import DriverUtils
from src.selenium_po.utils.excel_reader import ExcelReader


class TestCookieCheck:
    # 日志器
    logger = get_logger(
        log_name="TestCookieCheck",  # 使用类名作为日志器名称
        filename='./log/selenium-po.log',  # 所有类使用相同的日志文件
        level="INFO"  # 设置适当的日志级别
    )

    # 获取注册和登录所需要的测试数据
    reader = ExcelReader()
    cookie_check_test_data = reader.get_sheet_data_as_dict("LoginCookieCheckData")

    def setup_method(self):
        self.driver = DriverUtils.get_driver()
        self.driver.get("http://127.0.0.1:8080/cookie_check")
        self.cookie_check_page_operation = CookieCheckPageOperation(self.driver)

    def teardown_method(self):
        DriverUtils.quit_driver()

    @pytest.mark.order(3)
    @pytest.mark.parametrize("cookie_check_data", cookie_check_test_data)
    def test_cookie_check(self, cookie_check_data):
        # 从字典列表中取出测试数据
        expected_result = cookie_check_data["expectedResult"]

        try:
            time.sleep(1)
            DriverUtils.add_cookie()

            time.sleep(1)
            self.cookie_check_page_operation.click_cookie_check_button()

            time.sleep(1)
            assert self.cookie_check_page_operation.get_cookie_check_result() == expected_result



        except Exception as e:
            self.logger.error(f"检查登录态测试用例异常: {e}")
            raise
