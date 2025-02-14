from base.basepage import BasePage
from page.SettingPage.WifiPage import WifiPage


class NetWorkPage(BasePage):
    wifi = '//*[@text="无线网络"]'
    def goto_wifi_page(self):
        self.click_element(self.wifi)
        return WifiPage()