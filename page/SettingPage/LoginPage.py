from base.basepage import BasePage
from page.SettingPage.AccountLoginPage import AccountLoginPage


class LoginPage(BasePage):
    password_login_lab = '//*[@text="使用密码登录"]'

    def goto_account_login_page(self):
        self.click_element(self.password_login_lab)
        return AccountLoginPage
