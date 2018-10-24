#!/usr/bin/env python
# coding:GB18030

# Created by zhaohongwei on 2016-06-21
# Blog: http://blog.csdn.net/z_johnny

from logging.handlers import RotatingFileHandler
import logging
import threading
import yaml

class HwLogging(object):
    def __init__(self):
        self.logger = logging.getLogger()

        with open('./config/configLOG.yaml','rb') as config :
            self.allConfig = yaml.load(config)

        mythread=threading.Lock()
        mythread.acquire()
        # lock

        self.log_file_path = self.allConfig['LOGGING']['log_file_path']
        self.maxBytes = self.allConfig['LOGGING']['maxBytes']
        self.backupCount = self.allConfig['LOGGING']['backupCount']
        self.outputConsole_level = self.allConfig['LOGGING']['outputConsole_level']
        self.outputFile_level = self.allConfig['LOGGING']['outputFile_level']
        self.outputConsole = self.allConfig['LOGGING']['outputConsole']
        self.outputFile = self.allConfig['LOGGING']['outputFile']
        self.formatter = logging.Formatter('%(asctime)s  - %(filename)s : %(levelname)s  %(message)s')

        mythread.release()
        # unlock

    def outputLog(self):
        """
        output log to console and file
        """
        if self.outputConsole == 1 and not self.logger.handlers:
            # if true ,it should output log in console
            # if logger.handlers list is empty,add list,or writing log

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            self.logger.setLevel(self.outputConsole_level)
            self.logger.addHandler(console_handler)

            if self.outputFile == 1:
                self.file_handler = RotatingFileHandler(self.log_file_path, maxBytes=self.maxBytes, backupCount=self.backupCount)
                # defind RotatingFileHandler: log output path，single file max bytes, max backup number.
                self.file_handler.setFormatter(self.formatter)
                self.logger.setLevel(self.outputFile_level)
                self.logger.addHandler(self.file_handler)
            else:
                pass

        return self.logger

if __name__ == '__main__':
    #config_logging = './config/configLOG.yaml'
    mylog = HwLogging()
    logger = mylog.outputLog()


