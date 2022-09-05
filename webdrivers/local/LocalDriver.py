from .LocalDriverConfig import ChromeOptions
from selenium import webdriver



class LocalDriver(webdriver.Chrome):
    
    
    def __init__(self, webdriver_path: str, extensions=False) -> None:
        self.__options = ChromeOptions()
        self.__install_extensions(extensions)
        super().__init__(executable_path=webdriver_path, options=self.__install_extensions(extensions))
    
    def browser(self):
        return webdriver.Chrome()
    
    def __install_extensions(self, extensions):
        if extensions:
            self.__options.add_extensions_in_browser()

    