from selenium .webdriver.common.by import By
from selenium import webdriver

class LoginLocator:
    driver = webdriver.Chrome()
    username_input_loc = (By.ID,'username')
    passwd_input_loc = (By.ID,'password')
    login_btn_loc = (By.ID,'login-submit')
    forgot_passwd_loc = (By.CLASS_NAME,'lost_password')
    log_out_btn_loc = (By.CLASS_NAME,'logout')
    log_error_text_loc = (By.ID,'flash_error')
