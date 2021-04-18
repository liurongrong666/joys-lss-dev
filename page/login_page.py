import time

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    username_input = By.XPATH, '/html/body/div/div/div[1]/div[2]/div[1]/div/input'
    password_input = By.XPATH, '/html/body/div/div/div[1]/div[2]/div[2]/div/input'
    login_btn = By.XPATH,      "/html/body/div/div/div[1]/div[3]/button"
    def input_username(self, username): #  输入用户名
        return self.find_el(self.username_input).send_keys(username)
    def input_password(self, password): # 输入密码
        return self.find_el(self.password_input).send_keys(password)
    def click_login_btn(self): # 点击登录
        return self.find_el(self.login_btn).click()


