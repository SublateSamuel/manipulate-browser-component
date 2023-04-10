from manipule_browser.user_interface_browser import UserInterfaceBrowser
from manipule_browser.drivers.driver_types import DriverTypes
from manipule_browser.path import WEBDRIVER_DIR


browser = UserInterfaceBrowser(host=WEBDRIVER_DIR / 'chromedriver', browser_type=DriverTypes.LOCAL_CHROME)
browser.visit('https://google.com')


browser = UserInterfaceBrowser(host='http://selenoid:4444', browser_type=DriverTypes.REMOTE_CHROME)
browser.visit('https://google.com')