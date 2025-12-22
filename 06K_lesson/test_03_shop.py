from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))


def test_total_price():
    driver.get('https://www.saucedemo.com')
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.CLASS_NAME, 'submit-button').click()
    for items in ['sauce-labs-backpack', 'sauce-labs-bolt-t-shirt',
                  'sauce-labs-onesie']:
        driver.find_element(By.ID, f'add-to-cart-{items}').click()
    driver.find_element(By.ID, 'shopping_cart_container').click()
    driver.find_element(By.ID, 'checkout').click()
    driver.find_element(By.ID, 'first-name').send_keys('Standard')
    driver.find_element(By.ID, 'last-name').send_keys('User')
    driver.find_element(By.ID, 'postal-code').send_keys('233456')
    driver.find_element(By.ID, 'continue').click()
    total = driver.find_element(By.CLASS_NAME, 'summary_total_label').text
    driver.quit()
    assert 'Total: $58.29' in total, 'Неверная сумма'
