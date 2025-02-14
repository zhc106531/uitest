from base.basepage import BasePage
from page.SettingPage.AboutPage import AboutPage
from page.SettingPage.AccountAndSecurityPage import AccountAndSecurityPage
from page.SettingPage.NetWorkPage import NetWorkPage


class SettingPage(BasePage):
    net_work = '//*[@text="网络设置"]'# 网络设置
    account_and_security = '//*[@text="账号与安全"]'# 账号与安全
    about = '//*[@text="关于"]'# 关于

    def goto_network_page(self):
        self.click_element(self.net_work)
        return NetWorkPage()



    def goto_account_and_security_page(self):
        #去账号与安全页面
        self.double_click_element(self.account_and_security)
        return AccountAndSecurityPage()

    def goto_about_page(self):
        self.click_element(self.account_and_security)
        self.double_click_element(self.about)
        return AboutPage()


if __name__ == '__main__':
    set = SettingPage()
    set.goto_about_page()