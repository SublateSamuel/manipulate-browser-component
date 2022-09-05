from selenium import webdriver
import glob

class ChromeOptions(webdriver.ChromeOptions):


    def __init__(self):
        super().__init__()

    def capabilities(self):
        return  {
            "browserName": "chrome",
            "version": "95.0",
            "enableVNC": True,
            "enableVideo": False
            }
    
    def add_extensions_in_browser(self):
        extension = '*.crx'
        self.add_experimental_option("excludeSwitches", ['enable-automation'])
        try:
            files = glob.glob(f'.browser/extensions/{extension}')
            for f in files:
                self.add_extension(f)
        except Exception as err:
            raise err
