from base.basepage import BasePage
from page.SettingPage.LoginPage import LoginPage
class AccountAndSecurityPage(BasePage):
    xiaomi_account = '//*[@text="小米账号"]'
    def goto_login_page(self):
        self.click_element(self.xiaomi_account)
        return LoginPage