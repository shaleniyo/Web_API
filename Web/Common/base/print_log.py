import logging


def print_log():
    logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s')

    getlog = logging.getLogger(name='web_api_log')
    return getlog

logger  = print_log()

if __name__ == '__main__':
    logger.warning('warning message test')