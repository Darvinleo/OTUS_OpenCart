from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def __element(self, selector: tuple, index: int = 0):
        """return element by chosen search strategy"""
        return self.driver.find_elements(*selector)[index]

    def _click(self, selector, index=0):
        """click on selected element"""
        self._wait_for_visible(selector, index)
        ActionChains(self.driver).move_to_element(self.__element(selector, index)).click().perform()

    def _input(self, selector, value, index=0):
        element = self.__element(selector, index)
        element.clear()
        element.send_keys(value)

    def _wait_for_visible(self, selector, index=0, wait=5):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self.__element(selector, index)))

    def _wait_for_presence(self, selector):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(selector))

    def _get_element_text(self, selector, index=0):
        return self.__element(selector, index).text
