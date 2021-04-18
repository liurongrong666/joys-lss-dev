import time,pytest

from page.login_page import LoginPage
from utils.driver_util import DriverUtils

class TestLogin:

    def setup(self,):
        self.driver = DriverUtils.get_driver()
        self.login_page = LoginPage(self.driver)
        self.driver.maximize_window()
        self.driver.get("https://sy-dev.joysfintech.com/joys/login/pc_index.html?from=https%3A%2F%2Fsy-dev.joysfintech.com%2Fjoys%2Fpc_index.html%23%2F#/")
    def teardown(self):
        DriverUtils.quit_driver()

    def test_login(self):
        self.login_page.input_username('0139')   # 输入用户名
        time.sleep(2)
        self.login_page.input_password('kjjr588')  # 输入密码
        time.sleep(2)
        # self.login_page.click_login_btn()   # 点击登录按钮
        # time.sleep(2)

