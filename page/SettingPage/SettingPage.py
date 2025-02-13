from base.basepage import BasePage
from page.SettingPage.AccountAndSecurityPage import AccountAndSecurityPage


class SettingPage(BasePage):
    net_work = '//*[@text="网络设置"]'# 网络设置
    account_and_security = '//*[@text="账号与安全"]'# 账号与安全

    def goto_network_page(self):
        self.click_element(self.net_work)
        pass

    def goto_account_and_security_page(self):
        self.click_element(self.account_and_security)
        return AccountAndSecurityPage

if __name__ == '__main__':
    set = SettingPage()
    set.goto_network_page()