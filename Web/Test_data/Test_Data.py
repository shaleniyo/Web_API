

url = 'http://10.20.6.17:9000/login?back_url=http%3A%2F%2F10.20.6.17%3A9000%2F'

test_login_success = {'name':'登录正向用例','username':'contractor8@yingren.cn','password':'test123@88','msg':'Sign out'}

test_login_failed = [
    {'name':'登陆反向用例-密码错误','username':'contractor8@yingren.cn','password':'test123','error_msg':'无效的用户名或密码'}
]