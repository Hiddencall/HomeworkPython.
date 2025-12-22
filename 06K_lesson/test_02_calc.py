from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))
driver.get(
     'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

driver.find_element(By.ID, 'delay').clear()
driver.find_element(By.ID, 'delay').send_keys('45')


def test_calculator():
    for click_button in ['7', '+', '8', '=']:
        button = f'//span[text()="{click_button}"]'
        driver.find_element(By.XPATH, button).click()
    sum = WebDriverWait(driver, 50).until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'screen'), '15'))
    assert sum, 'сумма не пятнадцать'


driver.quit
