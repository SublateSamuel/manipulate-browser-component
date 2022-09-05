from selenium import webdriver
from webdrivers.remote.RemoteDriver import RemoteDriver
from webdrivers.local.LocalDriver import LocalDriver

class ConnectWithBrowserType:

    
    def __init__(self, host: str, remote_browser=False) -> None:
        self.__browser = self.__connect_with_browser(remote_browser, host)
    
    def __del__(self):
        self.__browser.quit()
    
    def __connect_with_browser(self, remote_browser: bool, host: str) -> webdriver.Chrome|webdriver.Remote:
        try:
            if remote_browser:
                return RemoteDriver(host=host)
            return LocalDriver(webdriver_path=host)
        except Exception as err:
            raise err

    @property
    def browser(self) -> webdriver.Chrome|webdriver.Remote:
        return self.__browser
    
    @property
    def session_id(self):
        return self.__browser.session_id
