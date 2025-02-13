from base.basepage import BasePage
from page.SettingPage.SettingPage import SettingPage
class AnyDoor(BasePage):
    def goto_seetting_page(self):
        self.start_app("com.android.settings")
        return SettingPage