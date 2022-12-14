import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', [
        'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
    ])
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    browser.implicitly_wait(25)
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Напишите ваш ответ здесь...']").send_keys(
        str(math.log(int(time.time()))))
    WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    browser.find_element(By.CLASS_NAME, "submit-submission").click()
    res = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
    assert res == 'Correct!', f"внимани, неожиданное сообщение '{res}'"

# pytest -v -s test_tmp.py
