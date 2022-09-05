import glob
from selenium.webdriver.chrome.options import Options

class ChromeOptions(Options):

    def __init__(self):
        super().__init__()

    def add_extensions_in_browser(self):
        extension = '*.crx'
        self.add_experimental_option("excludeSwitches", ['enable-automation'])
        try:
            files = glob.glob(f'.browser/extensions/{extension}')
            for f in files:
                self.add_extension(f)
        except Exception as err:
            raise err