from connection.ConnectBrowserType import ConnectWithBrowserType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserInterfaceBrowser(ConnectWithBrowserType):
    

    def __init__(self, host_executor: str, remote_browser=False) -> None:
        super().__init__(host=host_executor , remote_browser=remote_browser)
    
    @property
    def element_by(self):
        return By
    
    def visit(self, url):
        self.browser.get(url)
    
    def find_element(self, type_element: By, element_reference: str):
        return self.browser.find_element(type_element, element_reference)
    
    def find_all_elements(self, type_element: By, element_reference: str):
        return self.browser.find_elements(type_element, element_reference)
        
    def wait_element_on_screen(self, type_element: By, element_reference: str, timeout=10) -> bool:
        try:
            WebDriverWait(self.browser, timeout)\
            .until(EC.presence_of_element_located((type_element, element_reference)))
            return True
        except:
            return False
    
    def click_in_element(self, element):
        try:
            element.click()
        except Exception as err:
            raise err

    def send_text_in_element(self, element, text):
        try:
            element.send_keys(text)
        except Exception as err:
            raise err
