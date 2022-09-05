from selenium import webdriver
from .RemoteDriverConfig import ChromeOptions

class RemoteDriver(webdriver.Remote):
    
    def __init__(self, host: str, extensions=False) -> None:
        self.__options = ChromeOptions()
        self.__install_extensions(extensions)
        super().__init__(command_executor=host, desired_capabilities=self.__options.capabilities())
        
    
    def __install_extensions(self, extensions):
        if extensions:
            self.__options.add_extensions_in_browser()
