#!/usr/bin/python
# coding=utf-8

# Created by zhaohongwei on 2016-11-03
# Blog: http://blog.csdn.net/z_johnny

import unittest

class WebTest(unittest.TestCase):
    '''Web Test'''
    def setUp(self):
        print 'one'
    def tearDown(self):
        '''If setUp() succeeded, the tearDown() method will be run whether runTest() succeeded or not.'''
        print 'two'

    def test_Case1(self):
        self.assertEqual(1, 1, "Error")

    def test_Case2(self):
        self.assertNotEquals(2, 2, "Equals")

class APITest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Case1(self):
        print u'\n 1 不等于 2'
        self.assertEqual(1,2,"1 != 2")

    def test_Case2(self):
        self.assertEqual(3,3,"This's ok")

    def test_Case3(self):
        print 'APITest.test_Case3'
        self.assertEqual(5,6,'ERROR')

    def test_Case4(self):
        print "This's ok"
        self.assertEqual(3,3,"This's ok")

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(WebTest("test_Case1"))
    suite.addTest(APITest("test_Case2"))
    unittest.TextTestRunner().run(suite)
