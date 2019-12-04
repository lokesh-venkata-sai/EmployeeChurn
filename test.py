from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait


#This example requires Selenium WebDriver 3.13 or newer
with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 10)
    employee_fill = "http://127.0.0.1:5000"
    driver.get(employee_fill)
    driver.maximize_window()
    path = driver.find_element_by_class_name("employee_form").get_attribute("href")
    time.sleep(5)
    driver.get(path)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "p label:nth-of-type(1)"))
    )
    time.sleep(5)
    radio_buttons = driver.find_elements_by_css_selector("p label:nth-of-type(1)")
    for each in radio_buttons:
        each.click()
    driver.find_element_by_name("comments").send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
    driver.find_element_by_name("name").send_keys("John Doe")
    driver.find_element_by_name("email").send_keys("user@email.com")
    driver.find_element_by_name("eid").send_keys("111")
    driver.find_element_by_id("login_btn").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "demo"))
    )
    sucess = driver.find_elements_by_css_selector("demo")
    time.sleep(10)
