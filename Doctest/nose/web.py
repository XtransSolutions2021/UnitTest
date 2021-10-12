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

    search_text = "LambdaTest"
    search_box = driver.find_element(By.XPATH, "//input[@name='q']")
    search_box.send_keys(search_text)

    # Using Sleep is not a good programming practice
    # Only used here for demonstration purpose
    time.sleep(5)
    search_box.submit()

    time.sleep(5)

    # Click on the LambdaTest HomePage Link
    # This test will fail as the titles will not match
    title = "Most Powerful Cross Browser Testing Tool Online | LambdaTest"
    lt_link = driver.find_element(By.XPATH, "//h3[.='LambdaTest: Most Powerful Cross Browser Testing Tool Online']")
    lt_link.click()

    time.sleep(10)
    assert title == driver.title
    time.sleep(2)


@with_setup(setup_func, teardown_func)
def test_2():
    global driver
    print("test_2: Initiated")
    driver.get('https://lambdatest.github.io/sample-todo-app/')

    driver.find_element(By.NAME, "li1").click()
    driver.find_element(By.NAME, "li2").click()

    title = "Sample page - lambdatest.com"
    assert title == driver.title

    sample_text = "Happy Testing at LambdaTest"
    email_text_field = driver.find_element(By.ID, "sampletodotext")
    email_text_field.send_keys(sample_text)
    time.sleep(5)

    driver.find_element(By.ID, "addbutton").click()
    time.sleep(5)

    assert driver.find_element(By.XPATH, "//span[.='Happy Testing at LambdaTest']").text == sample_text