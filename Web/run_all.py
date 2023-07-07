import sys
import pytest
import os
from Common.base.read_config import read_config


BASE_DIR = os.path.dirname('__file__')
config_file_path = os.path.join(BASE_DIR,'Config/config.ini')
test_result_dir_path = read_config(config_file_path,'report','allure_results_dir_path')
test_report_dir_path = read_config(config_file_path,'report','test_report_dir_path')
img_dir_path = read_config(config_file_path,'image','image_dir_path')

