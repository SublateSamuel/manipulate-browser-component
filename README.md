# Browser Manipulation Remote or Local

> Python Component for RPA with Browser Access.

Browser component gives us the facility to define if we are going to use a local or remote browser wedriver by selenoid, just passing the local webdriver directory or the remote webdriver host.

## Index

1. [Resources and Technologies](#resources-and-technologies)
2. [Getting Started](#getting-started)
    1. [Requirements](#requirements)
    1. [Install](#install)
    1. [How to use](#how-to-use)


## Resources and Technologies

The component has the following technologies in its core.

- [Python 3.11](https://www.python.org/downloads/release/python-3100/) as main language
- [Selenium](https://selenium-python.readthedocs.io/) 
browser manipulation tools
## Getting Started

### Requirements

- Python 3.11^
- Poetry packeage manager
- Git
- Selenium Python Packed


### Install

1 — Clone the repository

```shell
git clone https://github.com/SublateSamuel/manipulate-browser-component
```

### How to use

inside the project root folder we will have the **UserInterfaceBrowser** class.

this class can be instantiated with the necessary parameters to start a browser

1 — necessary parameters for instantiated this class:

| Parameter          | type    | Descrição                                                                        |
|---------------|--------|------|
| `Host`          | string| host executor takes full path of local webdriver or host of remote webdriver                          |
| `Remote Browser`        | bool| if the webdriver is remote, this field must be **True** , parameter is **False** by default                               |

2 — Example using class as an instance local:

For this you need to have installed a **Chrome** or **Chromium** webdriver compatible with the browser version installed on your machine

```python
from manipule_browser.user_interface_browser import UserInterfaceBrowser
from manipule_browser.drivers.driver_types import DriverTypes
from manipule_browser.path import WEBDRIVER_DIR

browser = UserInterfaceBrowser(host=WEBDRIVER_DIR / 'chromedriver', browser_type=DriverTypes.LOCAL_CHROME)
browser.visit('https://google.com')


assert browser.title == "Google"

```

3 — Example using class as an instance remote:

For this you need have access to an infrastructure of remote browsers, for example: Selenoid

```python
from manipule_browser.user_interface_browser import UserInterfaceBrowser
from manipule_browser.drivers.driver_types import DriverTypes
from manipule_browser.path import WEBDRIVER_DIR

browser = UserInterfaceBrowser(host='http://selenoid:4444', browser_type=DriverTypes.LOCAL_CHROME)
browser.visit('https://google.com')


assert browser.title == "Google"

```