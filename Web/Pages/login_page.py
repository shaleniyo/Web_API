from Common.base.base import Base
from Locator.login_loc import LoginLocator

class LoginPage(Base):
    def login(self,username,password):
        self.send_data(LoginLocator.username_input_loc,username,'用户名输入框')
        self.send_data(LoginLocator.passwd_input_loc,password,'密码输入框')
        self.click_elemnt(LoginLocator.login_btn_loc,'登录按钮')
        self.wait(3)

    def get_login_erro_text(self,msg = ''):
        return self.get_elemnt_text(LoginLocator.forgot_passwd_loc,msg)

    def get_logout_text(self,msg = ''):
        return self.get_elemnt_text(LoginLocator.log_out_text_loc,msg)