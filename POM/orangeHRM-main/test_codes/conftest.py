import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as firefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture()
def setup():
    service = firefoxService(executable_path=GeckoDriverManager().install())
    return webdriver.firefox(service=service)