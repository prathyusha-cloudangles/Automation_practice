import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def base_class():
    driver = webdriver.Chrome()
    driver.get("http://52.1.189.42/testingAide/HP")
    driver.maximize_window()
    return driver

def login_invalid_creds(driver):
    #Fields taking little time to appear so adding an explicit wait
    wait = WebDriverWait(driver,10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[name='email']")))

    #To find the locators for email and password fields
    user_email = driver.find_element(By.CSS_SELECTOR,"input[name='email']")
    user_password = driver.find_element(By.CSS_SELECTOR,"input[name='password']")
    user_submit =driver.find_element(By.CLASS_NAME,"login_button__FZHj4")

    #to pass values into email and password fields
    user_email.send_keys("prathyusha.meka@gmail.com")
    user_password.send_keys("Test@123")
    user_submit.click()

    #to get the error message

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME,'p-toast-detail')))
    Error_toast=driver.find_element(By.CLASS_NAME,"p-toast-detail").text

    expected_error="Email does not exist."

    assert expected_error in Error_toast, f"Test Failed: expected '{expected_error}', but got '{expected_error}'"
    print("Test Passed: Error message displayed correctly")

    #adding assertions

    #print(Error_toast)

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

    #wait until teh website is fully loaded to get the changed url
    wait=WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ProjectCard_newProjectCard__lXM1u")))

    # to get the error message
    changed_url=driver.current_url
    expected_url="http://52.1.189.42/Projects"

    assert expected_url in changed_url, f"Test failed: Expected url is '{expected_url}' but got, '{changed_url}'"
    print("Test Passed: urls are matching")


def create_new_project(driver):
    wait=WebDriverWait(driver,10)
    wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='ProjectCard_newProjectCard__lXM1u']")))

    #locators and clickon 'create new project button'

    create_project_button = driver.find_element(By.XPATH,"//div[@class='ProjectCard_newProjectCard__lXM1u']")
    create_project_button.click()

    #provide the project name and description and create project
    project_name_field=driver.find_element(By.XPATH,"//input[@type='text'][1]")
    project_desc_field=driver.find_element(By.CLASS_NAME,"InputFieldLarge")
    project_name_field.send_keys("Test Project Automation")
    project_desc_field.send_keys("Test Project Description - Automation")
    project_save=driver.find_element(By.CLASS_NAME, "ConfirmButton")
    project_save.click()
    time.sleep(10)


    #to get all the project name in the page
    project_cards= driver.find_elements(By.CLASS_NAME,"ProjectCard_projectName__jIWqy")
    project_names=[project.text.strip() for project in project_cards]
    Expected_project_title = "Test Project Automation"

    # to assert the project creation
    assert Expected_project_title in project_names, F"Test Failed: Project '{Expected_project_title}' is not created"
    print("Test Passed: Project is created")

def Edit_project(driver):

    wait=WebDriverWait(driver,10)
    wait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Test Project Automation')]")))
    #To click on menu button (3dots)
    project_title=driver.find_element(By.XPATH,"//div[contains(text(),'Test Project Automation')]")
    menu_btn=project_title.find_element(By.XPATH, "following-sibling::div[3]")

    menu_btn.click()

    #to select the "Edit project" option
    edit_project_option=driver.find_element(By.XPATH,"//div[contains(text(), 'Edit Project')]")
    edit_project_option.click()

    #update the project name/description
    project_name_field = driver.find_element(By.CLASS_NAME,"InputFieldSmall")
    project_desc_field = driver.find_element(By.CLASS_NAME, "InputFieldLarge")

    project_name_field.click()
    project_name_field.clear()
    project_name_field.send_keys("Test Project Automation -Edit")

    project_desc_field.click()
    project_desc_field.clear()
    project_desc_field.send_keys("Test Project Automation description -Edit")

    project_save = driver.find_element(By.CLASS_NAME, "ConfirmButton")
    project_save.click()
    time.sleep(5)

    #to get all the project name in the page
    project_cards= driver.find_elements(By.CLASS_NAME,"ProjectCard_projectName__jIWqy")
    project_names=[project.text.strip() for project in project_cards]
    #print(project_names)
    Expected_project_title = "Test Project Automation -Edit"

    # to assert the project is edited
    assert Expected_project_title in project_names, f"Test Failed: Project title is not Edited to '{Expected_project_title}'"
    print("Test Passed: Project title is edited")



def delete_project(driver):
    #refreshing the page, as there is an issue where project is not getting deleted until page refresh
    driver.refresh()

    #wait unitl the project is loaded in home screen
    wait=WebDriverWait(driver,20)
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Test Project Automation -Edit')]")))

    # To click on menu button (3dots)
    project_title = driver.find_element(By.XPATH, "//div[contains(text(),'Test Project Automation -Edit')]")
    menu_btn = project_title.find_element(By.XPATH, "following-sibling::div[3]")
    menu_btn.click()


    # to select the "delete project" option
    delete_project_option = driver.find_element(By.XPATH, "//div[contains(text(), 'Delete Project')]")
    delete_project_option.click()
    confirm_btn=driver.find_element(By.XPATH,"//button[text()='Confirm']")
    confirm_btn.click()

  #to get all the project name in the page
    time.sleep(5)
    project_cards= driver.find_elements(By.CLASS_NAME,"ProjectCard_projectName__jIWqy")
    project_names=[project.text.strip() for project in project_cards]
    print(project_names)
    Expected_project_title = "Test Project Automation -Edit"

    # to assert the project creation
    assert Expected_project_title not in project_names, F"Test Failed: Project '{Expected_project_title}' is not deleted"
    print("Test Passed: Project is deleted")



driver=base_class()
#login_invalid_creds(driver)
login_valid_creds(driver)
create_new_project(driver)
Edit_project(driver)
delete_project(driver)