from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

input = driver.find_element(By.CSS_SELECTOR, '[type = "number"]')
driver.execute_script('arguments.type = "Text"', input)
input.send_keys('Sky')
sleep(5)
input.clear()
input.send_keys('Pro')
sleep(5)
driver.quit()
