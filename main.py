from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    try:
        link = "http://suninjuly.github.io/explicit_wait2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
        browser.find_element(By.ID, 'book').click()
        x = int(browser.find_element(By.ID, 'input_value').text)
        res = math.log(abs(12*math.sin(x)))
        browser.find_element(By.ID, 'answer').send_keys(res)
        browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
if __name__ == '__main__':
    main()
