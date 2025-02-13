from page.SettingPage.AccountAndSecurityPage import AccountAndSecurityPage
from page.anydoor.anydoor import AnyDoor as d

class Test:
    # 账号登录
    def test_01(self):
        d().goto_seetting_page().goto_account_and_security_page().goto_login_page().goto_account_login_page().account_login()

