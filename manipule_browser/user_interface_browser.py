from manipule_browser.connection.connect_with_browser import ConnectWithBrowser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from manipule_browser.drivers.driver_types import DriverTypes


class UserInterfaceBrowser(ConnectWithBrowser):

    def __init__(self, host: str, browser_type: DriverTypes, extensions=False, version='latest') -> None:
        super().__init__(host, browser_type, extensions,version)
    
    @property
    def element_by(self):
        return By
    
    def visit(self, url):
        self.browser.get(url)
        return self
    
    def find_element_by_xpath(self, element_reference: str):
        return self.browser.find_element(self.element_by.XPATH, element_reference)
    
    def find_all_elements_by_xpath(self, element_reference: str):
        return self.browser.find_elements(self.element_by.XPATH, element_reference)
        
    def wait_element_on_screen(self, type_element: By, element_reference: str, timeout=10) -> bool:
        try:
            WebDriverWait(self.browser, timeout)\
                .until(EC.presence_of_element_located((type_element, element_reference)))
            return True
        except:
            return False
    