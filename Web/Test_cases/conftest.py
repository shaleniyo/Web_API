import pytest
import os
from Test_data.Test_Data import url
from selenium import webdriver
from Pages.login_page import LoginPage
from Common.base.print_log import logger

chromedriver_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)),'chromedriver.exe'))

#print(chromedriver_path)
driver = None
@pytest.fixture(scope='session')
def handler():
    global driver
    logger.info('开始自动化测试')
    driver = webdriver.Chrome()
    lp =LoginPage()
    driver.maximize_window()
    driver.get(url)
    lp.wait(3)
    yield lp
    driver.quit()

@pytest.fixture()
def refresh_page():
    driver = webdriver.Chrome()
    driver.refresh()

