#!/usr/bin/python
# coding=UTF-8

# defind a class
# Logger
import logging
import sys
import os

dir_base = os.path.abspath(__file__)
dir_base = os.path.dirname(dir_base)
dir_base = os.path.dirname(dir_base)
sys.path.append(dir_base)


class Logger(object):
    logger = None

    def init_logger(self):
        self.logger = logging.getLogger(self.name)
        # 获取logger实例，如果参数为空则返回root logger

        # 指定logger输出格式
        formatter = logging.Formatter(
            '[ %(asctime)s - %(name)s - %(levelname)s - %(pathname)s - %(filename)s - %(module)s - %(funcName)s - %(lineno)d ]: %(message)s')

        # 文件日志
        v_mode = 'a'
        file_handler = logging.FileHandler(self.dir_base + "/logs/log_out.log", v_mode)
        file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式
        # 控制台日志
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.formatter = formatter  # 也可以直接给formatter赋值

        # 为logger添加的日志处理器
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

        # 指定日志的最低输出级别，默认为WARN级别
        self.logger.setLevel(logging.DEBUG)

    def get_logger(self):
        return self.logger

    def __init__(self, name, dir_base):
        self.name = name
        self.dir_base = dir_base
        self.init_logger()

    def __str__(self):
        pass

    @staticmethod
    def new_logger(name=''):
        c_logger = Logger(name, dir_base)
        logger = c_logger.get_logger()
        return logger
