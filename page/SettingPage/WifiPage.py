import time
from time import sleep

from base.basepage import BasePage
class WifiPage(BasePage):
    wifi_name = '//*[@text="ASU-wifi"]'
    password_inpt = '//*[@resource-id="com.android.settings:id/tv_wifi_edit"]'
    def find_wifi(self):
        index = 0
        while not self.is_element_exists(self.wifi_name):
            print(self.is_element_exists(self.wifi_name))
            self.press_key("DPAD_DOWN")
            self.press_key("DPAD_DOWN")
            index += 1
            if index > 20:
                break
        return self
    def link_wifi(self):
        self.find_wifi()
        self.click_if_element_exists(self.wifi_name)
        self.click_if_element_exists(self.wifi_name)
        self.input_text(self.password_inpt,'123456789')
        self.d.set_fastinput_ime(False)  # 恢复默认输入法
        self.press_key("DPAD_CENTER")
        time.sleep(1)
        self.click_percentage_coordinates(83,89)
        return self


if __name__ == '__main__':
    d= WifiPage()
    d.link_wifi()