from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base import init_db, insert_labs, print_all_products
init_db()

options = Options()
prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
}
options.add_experimental_option("prefs", prefs)
options.add_argument("--user-data-dir=C:/temp/selenium-profile")  
options.add_argument("--disable-extensions")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-notifications")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")
time.sleep(1)

try:
    logins = driver.find_elements(By.CLASS_NAME, "input_error.form_input")
    logins[0].send_keys("standard_user")
    logins[1].send_keys("secret_sauce")
    time.sleep(1)

    driver.find_element(By.ID, "login-button").send_keys(Keys.RETURN)
    time.sleep(1)

    wait = WebDriverWait(driver, 10)
    applogo = driver.find_element(By.CLASS_NAME, "app_logo").text

    if applogo == "Swag Labs":
        num_cards = len(driver.find_elements(By.CLASS_NAME, "inventory_item"))

        for i in range(num_cards):
            cards = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "inventory_item_name")))
            driver.execute_script("arguments[0].click();", cards[i])

            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_details_name")))
            name = driver.find_element(By.CLASS_NAME, "inventory_details_name").text.strip()

            insert_labs(name)

            driver.back()
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
            time.sleep(1)

    else:
        print("Ошибка")

except Exception as e:
    print("Ошибка:", e)

finally:
    driver.quit()
    print_all_products()
