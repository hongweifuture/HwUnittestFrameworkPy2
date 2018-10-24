#!/usr/bin/python
# coding=utf-8

# Created by zhaohongwei on 2016-11-03
# Blog: http://blog.csdn.net/z_johnny

import unittest

class JenkinsTest(unittest.TestCase):
    u'''python and jenkins'''
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Node(self):
        print 'This is node!'

    def test_Job(self):
        print 'This is job!'


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(JenkinsTest("test_Node"))
    unittest.TextTestRunner().run(suite)
