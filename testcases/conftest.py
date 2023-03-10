import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        ser_obj = Service('C:\\drivers\\chromedriver_win32\\chromedriver')
        ops = Options()
        ops.add_experimental_option('detach', True)
        driver = webdriver.Chrome(service=ser_obj, options=ops)

    elif browser=='firefox':
        ser_obj = Service('C:\\drivers\\geckodriver-v0.32.0-win64\\geckodriver')
        driver = webdriver.Firefox(service=ser_obj)

    elif browser=='edge':
        ser_obj = Service('C:\\drivers\\geckodriver-v0.32.0-win64\\geckodriver')
        driver = webdriver.Edge(service=ser_obj)

    driver.maximize_window()
    return driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

################### pytest html report ##################

#it is hook for adding environment info to html report


def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester Name'] = 'Akshay'

#it is hook for deleting/modifying environment info to html report


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)