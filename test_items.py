from selenium.webdriver.common.by import By
import time

def test_different_languages(l_browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    l_browser.get(link)
    time.sleep(30)

    assert l_browser.find_elements(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket"), "Button 'basket not found!'"
