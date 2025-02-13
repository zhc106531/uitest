import uiautomator2 as u2

class BasePage:
    def __init__(self, device_id=None):
        """初始化设备"""
        if device_id:
            self.d = u2.connect(device_id)
        else:
            self.d = u2.connect()
        self.d.implicitly_wait(10)  # 隐式等待10秒

    def click_element(self, xpath):
        """点击元素"""
        self.d.xpath(xpath).click()

    def input_text(self, xpath, text):
        """输入文本"""
        self.d.xpath(xpath).click()  # 先点击元素
        self.d.send_keys(text)  # 输入文本

    def verify_text_exists(self, text):
        """验证文本是否存在"""
        elements = self.d.xpath(f"//*[contains(@text, '{text}')]")
        return len(elements) > 0

    def scroll_to_element(self, xpath):
        """滚动到元素"""
        self.d.xpath(xpath).scrollIntoView()

    def get_element_text(self, xpath):
        """获取元素文本"""
        return self.d.xpath(xpath).get_text()

    def long_click_element(self, xpath):
        """长按元素"""
        self.d.xpath(xpath).long_click()

    def drag_element(self, from_xpath, to_xpath):
        """拖动元素"""
        self.d.xpath(from_xpath).drag_to(from_element=self.d.xpath(from_xpath), to_element=self.d.xpath(to_xpath))

    def start_app(self, package_name, activity_name=None):
        """启动应用
        - package_name: 应用的包名
        - activity_name: 启动的活动名（可选）
        """
        if activity_name:
            self.d.app_start(package_name, activity_name)
        else:
            self.d.app_start(package_name)
    def press_key(self, key_name):
        """
        模拟按下指定的按键。
        参数:
        d: uiautomator2的设备对象
        key_name: 按键名称，支持以下按键：
            - "HOME": 返回主页
            - "VOICE": 语音键
            - "VOLUME_UP": 音量加
            - "VOLUME_DOWN": 音量减
            - "MENU": 菜单键
            - "BACK": 返回键
            - "DPAD_UP": 向上键
            - "DPAD_DOWN": 向下键
            - "DPAD_LEFT": 向左键
            - "DPAD_RIGHT": 向右键
            - "DPAD_CENTER": 确认键
        """
        key_map = {
            "HOME": "KEYCODE_HOME",
            "VOICE": "KEYCODE_VOICE_ASSIST",
            "VOLUME_UP": "KEYCODE_VOLUME_UP",
            "VOLUME_DOWN": "KEYCODE_VOLUME_DOWN",
            "MENU": "KEYCODE_MENU",
            "BACK": "KEYCODE_BACK",
            "DPAD_UP": "KEYCODE_DPAD_UP",
            "DPAD_DOWN": "KEYCODE_DPAD_DOWN",
            "DPAD_LEFT": "KEYCODE_DPAD_LEFT",
            "DPAD_RIGHT": "KEYCODE_DPAD_RIGHT",
            "DPAD_CENTER": "KEYCODE_DPAD_CENTER"
        }

        if key_name in key_map:
            self.device.keyevent(key_map[key_name])
        else:
            raise ValueError(f"不支持的按键名称: {key_name}")

    def is_element_selected(self, xpath):
        """判断元素是否处于选中状态"""
        element = self.d.xpath(xpath)
        if element.exists:
            # 获取元素的selected属性
            selected = element.get().get('selected')
            return selected
        else:
            raise ValueError(f"Element with XPath '{xpath}' not found")

    def select_element_if_not_selected(self, xpath):
        """如果元素未被选中，则点击选中它"""
        if not self.is_element_selected(xpath):
            self.click_element(xpath)

    def deselect_element_if_selected(self, xpath):
        """如果元素已被选中，则点击取消选中它"""
        if self.is_element_selected(xpath):
            self.click_element(xpath)

if __name__ == '__main__':
    d = BasePage()
    d.start_app("com.android.settings")
    wz = '//*[@text="账号与安全"]'
    d.click_element(wz)