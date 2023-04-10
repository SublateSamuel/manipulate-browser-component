from selenium.webdriver.chrome.options import Options as ChromeOptions
from manipule_browser.path import EXTENSION_DIR
from manipule_browser.drivers.driver_types import DriverTypes
from selenium import webdriver


class LocalDriver():
    
    def __init__(self, host_executor: str, driver_type: DriverTypes, extensions: bool) -> None:
        self._driver = webdriver.Chrome if driver_type.LOCAL_CHROME.value else webdriver.Firefox
        self._install_extensions(extensions)
        self._browser = self._driver(executable_path=host_executor)
    
    @property
    def browser(self) -> webdriver:
        return self._browser
    
    def _install_extensions(self, driver_type: DriverTypes, extensions: bool) -> None:
        if driver_type.value == DriverTypes.LOCAL_CHROME.value:
            options = ChromeOptions()
            map(options.add_extension, EXTENSION_DIR.glob('*.crx')) if extensions else None


    