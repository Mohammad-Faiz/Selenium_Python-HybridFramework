from selenium import webdriver
from selenium.webdriver.common.by import By


def test_SearchValidProduct():
    driver = webdriver.Chrome()
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    driver.find_element(By.NAME, "search").send_keys("HP")
    driver.find_element(By.XPATH, "// *[ @ id = 'search'] / span / button").click()
    assert driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
    driver.quit()

def test_SearchInvalidProduct():
    driver = webdriver.Chrome()
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    driver.find_element(By.NAME, "search").send_keys("HONDA")
    driver.find_element(By.XPATH, "// *[ @ id = 'search'] / span / button").click()
    expt_text = "There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH, "//*[@id='content']/p[2]").text.__eq__(expt_text)
    driver.quit()

def test_SearchWithoutProduct():
    driver = webdriver.Chrome()
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    driver.find_element(By.NAME, "search")
    driver.find_element(By.XPATH, "// *[ @ id = 'search'] / span / button").click()
    expt_text = "There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH, "//*[@id='content']/p[2]").text.__eq__(expt_text)
    driver.quit()

