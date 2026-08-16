from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_01_form():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)
    # Откройте страницу в Edge или Safari.
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.maximize_window()

    First_name_input = wait.until(EC.presence_of_element_located((
        By.NAME, "first-name"))
    )
    First_name_input.send_keys("Иван")  # First name # Иван

    Last_name_input = driver.find_element(By.NAME, "last-name")
    Last_name_input.send_keys("Петров")  # Last name Петров

    Address_input = driver.find_element(By.NAME, "address")
    Address_input.send_keys("Ленина, 55-3")  # Address Ленина, 55-3

    Email_input = driver.find_element(By.NAME, "e-mail")
    Email_input.send_keys("test@skypro.com")  # Email test@skypro.com

    Phone_number_input = driver.find_element(By.NAME, "phone")
    Phone_number_input.send_keys(
        "+7985899998787")  # Phone number +7985899998787

    Zip_code_input = driver.find_element(By.NAME, "zip-code")
    Zip_code_input.send_keys("")  # Zip code *оставить пустым

    City_input = driver.find_element(By.NAME, "city")
    City_input.send_keys("Москва")  # City Москва

    Country_input = driver.find_element(By.NAME, "country")
    Country_input.send_keys("Россия")  # Country Россия

    Job_position_input = driver.find_element(By.NAME, "job-position")
    Job_position_input.send_keys("QA")  # Job position QA

    Company_input = driver.find_element(By.NAME, "company")
    Company_input.send_keys("SkyPro")  # Company SkyPro

    # Нажмите кнопку Submit.
    Submit_button = wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, ".btn-outline-primary"))
    )
    Submit_button.click()

    # Проверьте (assert), что поле Zip code подсвечено красным.
    zip_code_field = wait.until(
        EC.visibility_of_element_located((
            By.ID, "zip-code")))
    border_color = zip_code_field.value_of_css_property("border-color")
    assert border_color == "rgb(245, 194, 199)", f"Поле {
        zip_code_field} не подсвечено зеленым"

    # Проверьте (assert), что остальные поля подсвечены зеленым.
    fields = ["first-name",
              "last-name",
              "address",
              "city",
              "country",
              "e-mail",
              "phone",
              "job-position",
              "company"]

    for field_id in fields:
        field_element = wait.until(
            EC.visibility_of_element_located((
                By.ID, field_id)))
        border_color = field_element.value_of_css_property(
            "border-color")
        assert border_color == "rgb(186, 219, 204)", f"Поле {
            field_id} не подсвечено зеленым"

    driver.quit()
