import time
from base.basepage import BasePage
from page.SettingPage.DeveloperPage import DeveloperPage


class AboutPage(BasePage):
    kefu = '//*[@text="联系客服"]'
    device_info = '//*[@text="本机信息"]'
    device_name= '//*[@text="设备名称"]'
    developer = '//*[@text="开发者模式"]'

    def click_device_name_six(self):
        self.click_element(self.kefu)
        self.click_element(self.device_info)
        self.click_element(self.device_name)
        for i in range(7):
            self.press_key("DPAD_CENTER")
        return self

    def goto_developer_page(self):
        self.click_element(self.kefu)
        self.click_element(self.device_info)
        if self.is_element_exists(self.developer):
            self.double_click_element(self.developer)
        else:
            self.click_element(self.device_name)
            for i in range(7):
                self.press_key("DPAD_CENTER")
            self.double_click_element(self.developer)
        return DeveloperPage()

if __name__ == '__main__':
    d = AboutPage()