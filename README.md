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

- [Python 3.10](https://www.python.org/downloads/release/python-3100/) as main language
- [Selenium](https://selenium-python.readthedocs.io/) 
browser manipulation tools
## Getting Started

### Requirements

- Python 3.10^
- Git
- Selenium Python Packed

### Install

1 — Clone the repository

```shell
git clone git@github.com:SublateSamuel/manipulate-browser-component.git
```

### How to use

inside the project root folder we will have the **UserInterfaceBrowser** class.

this class can be instantiated with the necessary parameters to start a browser

1 — necessary parameters for instantiated this class:

| Parameter          | type    | Descrição                                                                        |
|---------------|--------|------|
| `Host Executor`          | string| host executor takes full path of local webdriver or host of remote webdriver                          |
| `Remote Browser`        | bool| if the webdriver is remote, this field must be **True** , parameter is **False** by default                               |

2 — Example using class as an instance local:

For this you need to have installed a **Chrome** or **Chromium** webdriver compatible with the browser version installed on your machine

```python
from UserInterfaceBrowser import UserInterfaceBrowser

web_interface = UserInterfaceBrowser(host_executor="my_full_path/local/webdriver.exe")

web_interface.visit("https.google.com")

assert web_interface.title == "Google"

```

3 — Example using class as an instance remote:

For this you need have access to an infrastructure of remote browsers, for example: Selenoid

```python
from UserInterfaceBrowser import UserInterfaceBrowser

web_interface = UserInterfaceBrowser(host_executor="http://localhost:4444", remote_browser=True)

web_interface.visit("https.google.com")

assert web_interface.title == "Google"

```
