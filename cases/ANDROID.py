#!/usr/bin/python
# coding=utf-8

# Created by zhaohongwei on 2016-11-03
# Blog: http://blog.csdn.net/z_johnny

import unittest
from source.HwLogging import HwLogging

class AndroidTest(unittest.TestCase):
    u'''用于Android测试'''
    def setUp(self):
        self.logging = HwLogging().outputLog()
        print 'use HwLogging'
        self.logging.warning('123456789')

    def tearDown(self):
        print 'Test Down'
        self.logging.info('Test Down')

    def test_Photo(self):
        self.assertEqual('jpg', 'png', "This is critical message")
        self.logging.critical('This is critical message')

    def test_Phone(self):
        self.logging.error('This is error message')
        self.logging.debug('This is debug message')

    def test_Calc(self):
        #self.logging.notset('This is notset message')
        print 'no notset message'
        raise IOError('This is not notset message!')

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(AndroidTest("test_Photo"))
    unittest.TextTestRunner().run(suite)
