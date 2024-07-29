import logging
import os.path

import pytest
from pytest import fixture
from appium.options.android import UiAutomator2Options
from appium import webdriver

from core.utils.readers import DeviceConfigManager


def pytest_configure(config):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(message)s'
    )


@fixture()
def driver():
    capabilities: dict = DeviceConfigManager("android11.json").configs
    options = UiAutomator2Options().load_capabilities(capabilities)
    _driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    _driver.implicitly_wait(10)
    yield _driver
    _driver.quit()
