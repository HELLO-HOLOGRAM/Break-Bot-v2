import logging
import os


class Logger:
    """
    预先封装好的日志模块，实例化后可以用这个类对指定文件输出日志\n
    同时可以指定输出日志的等级（默认是WARNING）

    需要传入参数：file：将日志输出到指定日志文件中，传入文件名\n
    可选传入参数：level：日志的输出等级，高于该等级的日志会被输出，默认为logging.INFO
    """

    def __init__(self, file: str, level=logging.INFO):
        # 检测到不存在logs文件夹就创建一个
        if not os.path.exists('./logs/'):
            os.mkdir('logs/')
        logging.basicConfig(filename='./logs/' + file,
                            format='%(asctime)s | %(levelname)s: %(message)s',
                            filemode='a',
                            level=level,
                            encoding='utf-8'
                            )

    def debug(self, msg: str):
        logging.debug(msg)
        pass

    def info(self, msg: str):
        logging.info(msg)
        pass

    def waring(self, msg: str):
        logging.warning(msg)
        pass

    def error(self, msg: str):
        logging.error(msg)
        pass

    def critical(self, msg: str):
        logging.critical(msg)
        pass
