import time
from typing import Dict

import pytest

from src.config.logging_config import get_logger
from src.selenium_po.operation.login_page_operation import LoginPageOperation
from src.selenium_po.utils.driver_utils import DriverUtils
from src.selenium_po.utils.excel_reader import ExcelReader


class TestLogin:
    """
    注册登录模块测试类

    调用注册登录页操作类LoginPageOperation的各个方法，以pytest参数化传入的测试数据作为参数，实现注册和登录功能
    """

    # 日志器
    logger = get_logger(
        log_name="TestLogin",  # 使用类名作为日志器名称
        filename='./log/selenium-po.log',  # 所有类使用相同的日志文件
        level="INFO"  # 设置适当的日志级别
    )

    # 获取注册和登录所需要的测试数据（用于@pytest.mark.parametrize装饰器进行参数化）
    reader = ExcelReader()
    register_test_data = reader.get_sheet_data_as_dict("RegisterData")
    login_test_data = reader.get_sheet_data_as_dict("LoginData")

    def setup_method(self) -> None:
        """
        setup_method特殊方法

        每个测试方法执行前都执行一次，调用浏览器管理工具类的方法打开浏览器并打开注册登录页
        """
        self.driver = DriverUtils.get_driver()
        self.driver.get("http://127.0.0.1:8080/login")
        self.login_page_operation = LoginPageOperation(self.driver)

    def teardown_method(self) -> None:
        """
        teardown_method特殊方法

        每个测试方法执行后都执行一次，调用浏览器管理工具类的方法关闭浏览器
        """
        DriverUtils.quit_driver()

    @pytest.mark.order(1)
    @pytest.mark.parametrize("register_data", register_test_data)
    def test_register(self, register_data: Dict[str, str]) -> None:
        """
        注册功能 测试用例

        测试过程中的time.sleep()暂停仅供调试使用，可酌情删除

        Args:
            register_data: 通过@pytest.mark.parametrize装饰器参数化，读取Excel文件获得的存放注册测试数据的字典
        """

        # 从字典中取出测试数据
        username = register_data["username"]
        password = register_data["password"]
        confirm_password = register_data["confirmPassword"]
        expected_result = register_data["expectedResult"]

        try:
            # 点击注册单选按钮
            time.sleep(1)
            self.login_page_operation.click_register_radio_button()

            # 输入账号
            time.sleep(1)
            self.login_page_operation.input_username(username)

            # 输入密码
            time.sleep(1)
            self.login_page_operation.input_password(password)

            # 输入确认密码
            time.sleep(1)
            self.login_page_operation.input_confirm_password(confirm_password)

            # 点击确认按钮
            time.sleep(1)
            self.login_page_operation.click_confirm_button()

            # 根据注册操作后页面上的提示信息进行断言
            time.sleep(1)
            assert self.login_page_operation.get_message() == expected_result



        except Exception as e:
            self.logger.error(f"注册测试用例异常: {e}")
            raise

    @pytest.mark.order(2)
    @pytest.mark.parametrize("login_data", login_test_data)
    def test_login(self, login_data: Dict[str, str]) -> None:
        """
        登录功能 测试用例

        测试过程中的time.sleep()暂停仅供调试使用，可酌情删除

        Args:
            login_data: 通过@pytest.mark.parametrize装饰器参数化，读取Excel文件获得的存放登录测试数据的字典
        """

        # 从字典中取出测试数据
        username = login_data["username"]
        password = login_data["password"]
        expected_result = login_data["expectedResult"]

        try:
            # 点击登录单选按钮
            time.sleep(1)
            self.login_page_operation.click_login_radio_button()

            # 清除账号输入框里的内容
            time.sleep(1)
            self.login_page_operation.clear_username()

            # 清除密码输入框里的内容
            time.sleep(1)
            self.login_page_operation.clear_password()

            # 输入账号
            time.sleep(1)
            self.login_page_operation.input_username(username)

            # 输入密码
            time.sleep(1)
            self.login_page_operation.input_password(password)

            # 点击确认按钮
            time.sleep(1)
            self.login_page_operation.click_confirm_button()

            # 根据登录操作后页面上的提示信息进行断言
            assert self.login_page_operation.get_message() == expected_result

            # 断言通过（登录成功）后，调用浏览器管理工具类的工具方法获取当前浏览器实例的所有cookie
            DriverUtils.get_all_cookies()

        except Exception as e:
            self.logger.error(f"登录测试用例异常: {e}")
            raise
