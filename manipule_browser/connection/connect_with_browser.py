from selenium import webdriver
from typing import Union
from manipule_browser.drivers.driver_types import DriverTypes
from manipule_browser.drivers.remote.remote_driver import RemoteDriver
from manipule_browser.drivers.local.local_driver import LocalDriver


class ConnectWithBrowser:

    def __init__(self, host: str, browser_type: DriverTypes, extensions: bool, version: str) -> None:
        self._browser = self._select_browser_by_driver_type(host, browser_type, extensions, version)

    @property
    def browser(self) -> webdriver.Chrome|webdriver.Remote:
        return self._browser
    
    @property
    def session_id(self) -> str:
        return self._browser.session_id
    
    def _select_browser_by_driver_type(self, host: str, driver_type: DriverTypes, extensions: bool, version: str) -> Union[RemoteDriver, LocalDriver]:
        if driver_type.name == DriverTypes.REMOTE_CHROME.name or DriverTypes.REMOTE_FIREFOX.name:
            return RemoteDriver(host, driver_type, extensions, version)
        elif driver_type.name == DriverTypes.LOCAL_CHROME.name or DriverTypes.LOCAL_FIREFOX.name:
            return LocalDriver(host, driver_type, extensions)
        raise Exception('Doe not implemented browser type')

    