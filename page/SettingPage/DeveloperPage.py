from base.basepage import BasePage

class DeveloperPage(BasePage):
    adb = '//*[@text="ADB调试"]'

    # def adb_on(self):
    #     self.click_element(self.adb)
    #     self.press_key("DPAD_DOWN")
    #     self.press_key("DPAD_DOWN")
    #     self.press_key("DPAD_CENTER")
    #     return self

    def adb_off(self):
        self.click_element(self.adb)
        self.click_if_element_exists(self.adb)
        self.press_key("DPAD_UP")
        self.press_key("DPAD_UP")
        self.press_key("DPAD_CENTER")
        return self

if __name__ == '__main__':
    d = DeveloperPage()
    d.adb_off()