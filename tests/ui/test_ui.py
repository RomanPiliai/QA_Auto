import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



@pytest.mark.ui
def test_check_incorrect_username():
    
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    
    driver.get("https://github.com/login")
    
    login_elem = driver.find_element("id", "login_field")
    
    login_elem.send_keys("roman@fakeemail.com")
    
    pass_elem = driver.find_element("id", "password")
    
    pass_elem.send_keys("wrong password")
    
    btn_elem = driver.find_element("name", "commit")
    
    btn_elem.click()
    
    
    assert driver.title == "Sign in to GitHub · GitHub"
    
    driver.close()