from selenium.webdriver.common.by import By
from selenium import webdriver

class Change_PWD:
    driver = webdriver.Chrome()
    email_input_loc = (By.ID,'mail')
    submit_btn_loc = (By.NAME,'commit')
    err_email_user_loc = (By.ID,'flash_error')