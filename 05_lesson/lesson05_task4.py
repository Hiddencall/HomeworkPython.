from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

input1 = driver.find_element(By.CSS_SELECTOR, '[id = "username"]')
input1.send_keys('tomsmith')
input2 = driver.find_element(By.CSS_SELECTOR, '[id = "password"]')
input2.send_keys('SuperSecretPassword!')
sleep(5)
button = driver.find_element(By.CSS_SELECTOR, 'button.radius')
button.click()
text_result = driver.find_element(By.CSS_SELECTOR,
                                  "#flash-messages").text[0:-2]
print(text_result)
driver.quit()
