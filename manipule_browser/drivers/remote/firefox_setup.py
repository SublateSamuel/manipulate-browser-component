from selenium import webdriver


class FirefoxSetup(webdriver.FirefoxOptions):

    def __init__(self, version: str):
        self._version = version
    
    def capabilities(self,
        name_connection=None,
        enable_vnc=True, 
        enable_video=False,
        browser_name='browser_rec'
        ):
        return {
            "browserName": "firefox",
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

