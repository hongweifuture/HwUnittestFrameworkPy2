#!/usr/bin/env python
# coding=utf-8

# Created by zhaohongwei on 2016-11-05
# Change yaml config file on 20181023
# Blog: http://blog.csdn.net/z_johnny

from source.HwCleanPyc import HwCleanPyc
from source.HwSendEmail import HwSendEmail
from source.HwCutfile import HwFileMove
from source.HwUnittest import HwStartup
import unittest
import time
'''
Usage: 



'''

if __name__ == '__main__':
    suite = unittest.TestSuite()

    # HwStartup(suite, 'CN') , you must choose
    # you must choose CN or EN,it's report language
    HwStartup(suite, 'EN').startup()

    # send email , you can choose
    ISOTIMEFORMAT='_%Y-%m-%d_%A'
    current_time =str(time.strftime(ISOTIMEFORMAT))
    email_tiltle = 'johnny test'+'%s'%current_time       # as johnny test_2016-06-20_Monday
    email_content = u'本轮自动化测试完成，详情请查看附件，本邮件是程序自动发送，请勿回复！'
    #HwSendEmail(email_tiltle,email_content).sendemail()

    time.sleep(5)
    # HwFileMove() move result to report , you can choose
    HwFileMove().moveFile()

    time.sleep(5)
    # delde pyc , you can choose
    HwCleanPyc().cleanPyc()







