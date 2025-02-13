from base.basepage import BasePage
class AccountLoginPage(BasePage):
    account = '//*[@resource-id="com.xiaomi.account:id/login_edit_user"]'
    password= '//*[@resource-id="com.xiaomi.account:id/login_edit_pwd"]'
    login_btn = '//*[@text="立即登录"]'
    def account_login(self):
        self.input_text(self.account,'15222154902')
        self.input_text(self.password,'zhc106531')
        self.click_element(self.login_btn)

if __name__ == '__main__':
    d= AccountLoginPage()
    d.account_login()