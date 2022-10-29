import time
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_selected_language_and_the_presence_of_a_button(browser):
    browser.get(link)
    time.sleep(30)
    try:
        btn = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
        assert btn is not None, "Кнопка найдена"
    finally:
        browser.quit()
