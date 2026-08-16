from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_02_form():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 50)
    # Откройте страницу в Google Chrome.
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.maximize_window()

    # В поле ввода по локатору #delay введите значение 45.
    delay_input = wait.until(
         EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
     )
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажимаем кнопку "7"
    btn_7 = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//div[@class='keys']//span[text()='7']")))
    btn_7.click()

    # Нажимаем кнопку "+"
    btn_plus = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//div[@class='keys']//span[text()='+']")))
    btn_plus.click()

    # Нажимаем кнопку "8"
    btn_8 = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//div[@class='keys']//span[text()='8']")))
    btn_8.click()

    # Нажимаем кнопку "="
    btn_equals = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//div[@class='keys']//span[text()='=']")))
    btn_equals.click()

    # Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.
    result = wait.until(EC.text_to_be_present_in_element((
        By.CSS_SELECTOR, ".screen"), "15")
    )

    assert result

    driver.quit()
