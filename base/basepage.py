import time

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
        time.sleep(0.5)

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

    def is_element_exists(self, xpath):
        """判断元素是否存在"""
        element = self.d.xpath(xpath)
        return element.exists

    def click_if_element_exists(self, xpath):
        """如果元素存在就点击"""
        if self.is_element_exists(xpath):
            self.click_element(xpath)

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
            self.d.keyevent(key_map[key_name])
        else:
            raise ValueError(f"不支持的按键名称: {key_name}")
        time.sleep(0.2)

    def double_click_element(self, xpath,t = 0.2):
        """双击元素"""
        element = self.d.xpath(xpath)
        # 获取元素的边界信息
        element.click()
        time.sleep(t)
        element.click()
        time.sleep(0.5)

    def is_toast_exists(self, text, timeout=2):
        """检测toast是否存在
        :param text: toast的文本内容
        :param timeout: 超时时间，默认为20秒
        :return: 如果toast存在返回True，否则返回False
        """
        start_time = time.time()
        timeout = float(timeout)  # 确保timeout是浮点数
        while time.time() - start_time < timeout:
            try:
                toast_text = self.d.toast.get_message()  # 获取toast消息
                print("获取到toast：",toast_text)
                if text in toast_text:
                    return True
            except Exception as e:
                # 捕获异常，可能是toast还未出现
                pass
            time.sleep(0.5)  # 每隔0.5秒尝试一次
        print(f"获取toast超时，未找到包含 '{text}' 的toast")
        return False

    def click_coordinates(self, x, y):
        """点击指定坐标
        :param x: x坐标
        :param y: y坐标
        """
        self.d.click(x, y)

    def click_percentage_coordinates(self, x_percentage, y_percentage):
        """
        点击百分比坐标
        :param x_percentage: x坐标的百分比，范围0-100
        :param y_percentage: y坐标的百分比，范围0-100
        """
        # 获取设备屏幕的宽高
        width, height = self.d.window_size()
        # 计算实际的坐标
        x = int(width * x_percentage / 100)
        y = int(height * y_percentage / 100)
        # 点击计算后的坐标
        self.d.click(x, y)

if __name__ == '__main__':
    d = BasePage()
    d.start_app("com.android.settings")
    wz = '//*[@text="账号与安全"]'
    d.click_element(wz)