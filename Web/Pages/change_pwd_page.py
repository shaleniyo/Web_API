from Common.base.base import Base
from Locator.Change_pwd_loc import Change_PWD

class ChangePwdPage(Base):

    def Submit_Email(self,email,):
        self.send_data(Change_PWD.email_input_loc,email,'email输入框')
        self.click_elemnt(Change_PWD.submit_btn_loc,'提交按钮')

    def get_submit_error_text(self,msg = ''):
        self.get_elemnt_text(Change_PWD.err_email_user_loc,msg)