import time
from time import sleep
from Common.base.print_log import logger
from run_all import img_dir_path


class Base:
    def __int__(self, driver):
        self.driver = driver

    def wait(self, time):
        sleep(time)

    def search_elemnt(self, loc, msg=''):
        logger.info(f'开始查找页面元素：{msg}')
        try:
            element = self.driver.find_element(loc)
            logger.info(f'找到页面元素{loc}')
            return element
        except Exception as e:
            raise e

    def click_elemnt(self, loc, msg=''):
        logger.info(f'开始点击元素:{msg}')
        self.search_elemnt(loc, msg).click()

    def send_data(self, loc, data, msg=''):
        self.search_elemnt(loc, msg).send_keys(data)
        logger.info(f'向页面发送了数据:{data}')

    def get_elemnt_text(self, loc, msg=''):
        text = self.search_elemnt(loc, msg).text
        logger.info(f'获取元素文本:{msg}')
        return text

    def save_picture(self, msg=''):
        img_file_path = img_dir_path + '{0}-{1}.png'.format(msg, time.strftime('%Y-%m-%d_%H_%S_%S', time.localtime()))

        try:
            self.driver.save_screenshot(img_file_path)
            logger.info(f'截图保存成功，保存路径为:{img_file_path}')

        except Exception as e:
            logger.warning(f'截图失败:{msg}')
            raise e
