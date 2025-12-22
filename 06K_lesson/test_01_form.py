from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By

edge_driver_path = r"C:\Users\wert\edgedriver_win64\msedgedriver.exe"
driver = webdriver.Edge(service=EdgeService(edge_driver_path))

driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys("Иван")
driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys("Петров")
driver.find_element(By.CSS_SELECTOR,
                    '[name="address"]').send_keys("Ленина, 55-3")
driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]').clear()
driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys("Москва")
driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys("Россия")
driver.find_element(By.CSS_SELECTOR,
                    '[name="e-mail"]').send_keys("test@skypro.com")
driver.find_element(By.CSS_SELECTOR,
                    '[name="phone"]').send_keys("+7985899998787")
driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys("QA")
driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()


def test_zip_code_field():
    zip_code = driver.find_element(By.ID, 'zip-code')
    class_zip_code = zip_code.get_attribute('class')
    assert 'alert-danger' in class_zip_code, "Поле не красное"


def test_another_field():
    for field_id in ['first-name', 'last-name', 'address', 'city', 'country',
                     'e-mail', 'phone', 'job-position', 'company']:
        field = driver.find_element(By.ID, field_id)
        class_field = field.get_attribute('class')
    assert 'alert-succes' in class_field, "Поле не зеленое"


driver.quit
