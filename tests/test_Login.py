from selenium import webdriver
from selenium.webdriver.common.by import By


def test_LoginValid():
    driver = webdriver.Chrome()
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//*[@id='top-links']/ul/li[2]/a/span[1]").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    driver.find_element(By.NAME, "email").send_keys("demo11108@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("12345")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    assert driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()


def test_LoginInvalid():
    driver = webdriver.Chrome()
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//*[@id='top-links']/ul/li[2]/a/span[1]").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    driver.find_element(By.NAME, "email").send_keys("demo111@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("12345")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    assert driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()
    driver.quit()