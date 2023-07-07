import os
import sys
import configparser
from Common.base.print_log import print_log

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


def read_config(configc_file_path, field, key):
    cf = configparser.ConfigParser()
    try:
        cf.read(configc_file_path,encoding='utf-8')
        result = cf.get(field,key).replace('base_dir',BASE_DIR).replace('\\','/') #转换linux的路径
        if ':' in result:
            result = cf.get(field,key).replace('base_dir',BASE_DIR).replace('/','\\') #转换window路径
    except Exception as e:
        logger = print_log()
        logger.error(e)
        sys.exit(1)
    return result

if __name__ == '__main__':
    config_file_path = os.path.join(BASE_DIR,'Config/config.ini')
    img_dir_path = read_config(config_file_path,'image','image_dir_path')
    allure_results_dir_path = read_config(config_file_path,'report','allure_results_dir_path')
