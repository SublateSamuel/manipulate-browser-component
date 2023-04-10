from selenium import webdriver


class FirefoxSetup(webdriver.FirefoxOptions):

    def __init__(self, version: str):
        self._version = version


    def options(self):
        self.add_argument('browserName', 'firefox')
        self.add_argument('version', self._version)
        return self
    
    def capabilities(self,
        name_connection=None, 
        enable_vnc=True, 
        enable_video=True,
        browser_name='browser_rec'
        ):
        return {"selenoid:options": {
                    "enableVNC": enable_vnc,
                    "name": name_connection,
                    "screenResolution": "1280x1024x24",
                    "enableVideo": enable_video,
                    "videoName": f"{browser_name}.mp4",
                    "videoScreenSize": "1280x1024"
                }
            }

