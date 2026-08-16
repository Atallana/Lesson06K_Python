from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_03_shop():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    # Откройте сайт магазина в FireFox.
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Авторизуйтесь как пользователь standard_user.
    Username_input = wait.until(EC.presence_of_element_located(
               (By.ID, "user-name"))
    )
    Username_input.send_keys("standard_user")

    Password_input = driver.find_element(By.ID, "password")
    Password_input.send_keys("secret_sauce")

    Login = wait.until(EC.element_to_be_clickable((
            By.ID, "login-button"))
    )
    Login.click()

    # Добавьте в корзину товары:
    # Sauce Labs Backpack.
    Sauce_Labs_Backpack = wait.until(EC.element_to_be_clickable((
        By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    Sauce_Labs_Backpack.click()

    # Sauce Labs Bolt T-Shirt.
    Sauce_Labs_Bolt_T_Shirt = wait.until(EC.element_to_be_clickable((
        By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))
    )
    Sauce_Labs_Bolt_T_Shirt.click()

    # Sauce Labs Onesie.
    Sauce_Labs_Onesie = wait.until(EC.element_to_be_clickable((
        By.ID, "add-to-cart-sauce-labs-onesie"))
    )
    Sauce_Labs_Onesie.click()

    # Перейдите в корзину.
    Shopping_cart_link = wait.until(EC.element_to_be_clickable((
        By.CLASS_NAME, "shopping_cart_link"))
    )
    Shopping_cart_link.click()

    # Нажмите Checkout.
    Checkout = wait.until(EC.element_to_be_clickable((
            By.ID, "checkout"))
    )
    Checkout.click()

    # Заполните форму своими данными:
    # имя,
    First_name_input = wait.until(EC.presence_of_element_located(
           (By.ID, "first-name"))
    )
    First_name_input.send_keys("Татьяна")

    # фамилия,
    Last_name_input = driver.find_element(By.ID, "last-name")
    Last_name_input.send_keys("Черкасова")

    # почтовый индекс.
    Postal_code_input = driver.find_element(By.ID, "postal-code")
    Postal_code_input.send_keys("185016")

    # Нажмите кнопку Continue.
    Continue = wait.until(EC.element_to_be_clickable((
        By.ID, "continue"))
    )
    Continue.click()

    # Прочитайте со страницы итоговую стоимость (Total).
    wait.until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, ".summary_total_label"))
    )

    # Проверьте, что итоговая сумма равна $58.29.
    Total = wait.until(
        EC.text_to_be_present_in_element((
            By.CSS_SELECTOR, ".summary_total_label"), "$58.29")
    )

    assert Total

    # Закройте браузер.
    driver.quit()
