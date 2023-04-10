from selenium import webdriver
from manipule_browser.path import EXTENSION_DIR


class ChromeSetup(webdriver.ChromeOptions):

    def __init__(self, extension: bool, version: str):
        super().__init__()
        self._version = version
        self.add_extensions_in_browser() if extension else None
    
    def capabilities(self, name_connection=None, enable_vnc=True, enable_video=True, browser_name='browser_rec'
        ):
        return {
            "browserName": "chrome",
            "version": self._version,
            "selenoid:options": {
                "enableVNC": enable_vnc,
                "name": name_connection,
                "screenResolution": "1280x1024x24",
                "enableVideo": enable_video,
                "videoName": f"{browser_name}.mp4",
                "videoScreenSize": "1280x1024"
            }
        }

    def add_extensions_in_browser(self):
        self.add_experimental_option("excludeSwitches", ['enable-automation'])
        map(self.add_extension, EXTENSION_DIR.glob('*.crx'))

