import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def base_class():
    driver = webdriver.Chrome()
    driver.get("http://52.1.189.42/testingAide/HP")
    driver.maximize_window()
    time.sleep(5)
    return driver

def login_invalid_creds(driver):
    #to find the locators for email and password fields
    user_email = driver.find_element(By.CSS_SELECTOR,"input[name='email']")
    user_password = driver.find_element(By.CSS_SELECTOR,"input[name='password']")
    user_submit =driver.find_element(By.CLASS_NAME,"login_button__FZHj4")

    #to pass values into email and password fields
    user_email.send_keys("prathyusha.meka@gmail.com")
    user_password.send_keys("Test@123")
    user_submit.click()
    time.sleep(5)

    #to get the error message
    Error_toast=driver.find_element(By.CLASS_NAME,"p-toast-detail").text
    print(Error_toast)

def login_valid_creds(driver):
    # to find the locators for email and password fields
    user_email = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
    user_password = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
    user_submit = driver.find_element(By.CLASS_NAME, "login_button__FZHj4")

    # to pass values into email and password fields
    user_email.clear()
    user_password.clear()
    user_email.send_keys("prathyusha.meka@cloudangles.com")
    user_password.send_keys("Test@123")
    user_submit.click()
    time.sleep(5)

    # to get the error message
    new_url=driver.current_url
    print(new_url)

def create_new_project(driver):
    #locators and clickon 'create new project button'
    create_project_button = driver.find_element(By.XPATH,"//div[@class='ProjectCard_newProjectCard__lXM1u']")
    create_project_button.click()

    #provide the project name and description
    project_name_field=driver.find_element(By.XPATH,"//input[@type='text'][1]")
    project_desc_field=driver.find_element(By.CLASS_NAME,"InputFieldLarge")
    project_name_field.send_keys("Test Project Automation")
    project_desc_field.send_keys("Test Project Automation")

    project_save=driver.find_element(By.CLASS_NAME, "ConfirmButton")
    project_save.click()
    time.sleep(10)

driver=base_class()
login_invalid_creds(driver)
login_valid_creds(driver)
create_new_project(driver)