import pytest
from Test_data.Test_Data import test_login_success
from Test_data.Test_Data import test_login_failed
from Common.base.print_log import logger
import allure


@allure.epic('weblogin_project')
@allure.feature('登陆模块测试')
@pytest.mark.usefixtures('refresh_page')
class TestLogin:

    @allure.story('登录模块-正常测试')
    @allure.title('登录-正向用例')
    @pytest.mark.last
    def test_login_success(self,handler):
        logger.info('测试开始')
        with allure.step('开始执行登录操作：'):
            allure.attach(f'发送用户名：{test_login_success["username"]}')
            allure.attach(f'发送密码：{test_login_success["password"]}')
            allure.attach('点击登录')
            handler.login(test_login_success["username"],test_login_success["password"])
            assert test_login_success['msg'] == handler.get_logout_text('退出文本')

    @allure.epic('登录模块-异常测试')
    @allure.title('登录-反向用例')
    @pytest.mark.parametrize('data',test_login_failed)
    def test_login_failed(self,handler,data):
        allure.attach(f'发送用户名：{test_login_failed["username"]}')
        allure.attach(f'发送密码：{test_login_failed["password"]}')
        allure.attach('点击登录')
        handler.login(test_login_failed["username"],test_login_failed["password"])
        assert data['error_msg'] == handler.get_login_erro_text('获取账号密码错误文本')
