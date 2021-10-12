from nose.tools import with_setup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def setup_func():
    global driver
    print("setup_func: setUp Method called")
    driver = webdriver.Chrome()
    driver.maximize_window()


def teardown_func():
    global driver
    print("teardown_func: Teardown Method called")
    driver.quit()


@with_setup(setup_func, teardown_func)
def test_1():
    global driver
    print("test_1: Initiated")
    driver.get('https://www.google.com')
    title = "Google"
    assert title == driver.title
