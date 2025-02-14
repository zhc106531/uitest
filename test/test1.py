from page.SettingPage.AccountAndSecurityPage import AccountAndSecurityPage
from page.anydoor.anydoor import AnyDoor as d

class Test:
    # 账号登录
    def test_loging(self):
        """
        登录
        """
        d().goto_seetting_page().goto_account_and_security_page().goto_login_page().goto_account_login_page().account_login()
    def test_adb_off(self):
        """
        关闭开发者选项
        :return:
        """
        d().goto_seetting_page().goto_about_page().click_device_name_six().goto_developer_page().adb_off()
    def test_link_work(self):
        """
        链接网络
        :return:
        """
        d().goto_seetting_page().goto_network_page().goto_wifi_page().link_wifi()