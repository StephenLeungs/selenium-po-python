from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def find_ele(self, ele):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(lambda x: x.find_element(ele[0], ele[1]))
        return element

    def input(self, ele, text):
        self.find_ele(ele).send_keys(text)

    def clear_text(self, ele):
        self.find_ele(ele).clear()

    def click(self, ele):
        self.find_ele(ele).click()

    def switch_to_frame(self, frame_reference):
        self.driver.switch_to.frame(frame_reference)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def get_text(self, ele):
        msg = self.find_ele(ele)
        return msg.text

    def select_check(self, ele):
        element = self.find_ele(ele)
        if not (element.is_selected()):
            element.click()
