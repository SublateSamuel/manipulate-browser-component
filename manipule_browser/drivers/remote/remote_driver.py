from typing import Union
from selenium import webdriver
from .chrome_setup import ChromeSetup
from .firefox_setup import FirefoxSetup
from manipule_browser.drivers.driver_types import DriverTypes


class RemoteDriver(webdriver.Remote):
    
    def __init__(self, host: str, driver_type: DriverTypes, extensions: bool, version: str) -> None:
        self._setup_driver = self._select_options_by_driver_type(extensions, version, driver_type)
        super().__init__(
            command_executor=host, 
            desired_capabilities=self._setup_driver.capabilities()
            )
        
    def _select_options_by_driver_type(self, extensions: str, version: str, driver_type: DriverTypes) -> Union[ChromeSetup, FirefoxSetup]:
        if driver_type.value == DriverTypes.REMOTE_CHROME.value:
            return ChromeSetup(extensions, version)
        elif driver_type.value == DriverTypes.REMOTE_FIREFOX.value: 
            return FirefoxSetup(version)
        raise Exception('Doe not implemented browser type')
