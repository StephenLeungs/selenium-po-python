import time

import pytest

from src.config.logging_config import get_logger
from src.selenium_po.operation.login_page_operation import LoginPageOperation
from src.selenium_po.utils.driver_utils import DriverUtils
from src.selenium_po.utils.excel_reader import ExcelReader


class TestLogin:
    # 日志器
    logger = get_logger(
        log_name="TestLogin",  # 使用类名作为日志器名称
        filename='./log/selenium-po.log',  # 所有类使用相同的日志文件
        level="INFO"  # 设置适当的日志级别
    )

    # 获取注册和登录所需要的测试数据
    reader = ExcelReader()
    register_test_data = reader.get_sheet_data_as_dict("RegisterData")
    login_test_data = reader.get_sheet_data_as_dict("LoginData")

    def setup_method(self):
        self.driver = DriverUtils.get_driver()
        self.driver.get("http://127.0.0.1:8080/login")
        self.login_page_operation = LoginPageOperation(self.driver)

    def teardown_method(self):
        DriverUtils.quit_driver()

    @pytest.mark.order(1)
    @pytest.mark.parametrize("register_data", register_test_data)
    def test_register(self, register_data):
        # 从字典列表中取出测试数据
        username = register_data["username"]
        password = register_data["password"]
        confirm_password = register_data["confirmPassword"]
        expected_result = register_data["expectedResult"]

        try:
            time.sleep(1)
            self.login_page_operation.click_register_radio_button()

            time.sleep(1)
            self.login_page_operation.input_username(username)

            time.sleep(1)
            self.login_page_operation.input_password(password)

            time.sleep(1)
            self.login_page_operation.input_confirm_password(confirm_password)

            time.sleep(1)
            self.login_page_operation.click_confirm_button()

            time.sleep(1)
            assert self.login_page_operation.get_message() == expected_result



        except Exception as e:
            self.logger.error(f"注册测试用例异常: {e}")
            raise

    @pytest.mark.order(2)
    @pytest.mark.parametrize("login_data", login_test_data)
    def test_login(self, login_data):
        # 从字典列表中取出测试数据
        username = login_data["username"]
        password = login_data["password"]
        expected_result = login_data["expectedResult"]

        try:
            time.sleep(1)
            self.login_page_operation.click_login_radio_button()

            time.sleep(1)
            self.login_page_operation.clear_username()

            time.sleep(1)
            self.login_page_operation.clear_password()

            time.sleep(1)
            self.login_page_operation.input_username(username)

            time.sleep(1)
            self.login_page_operation.input_password(password)

            time.sleep(1)
            self.login_page_operation.click_confirm_button()

            assert self.login_page_operation.get_message() == expected_result

            DriverUtils.get_all_cookies()

        except Exception as e:
            self.logger.error(f"登录测试用例异常: {e}")
            raise
