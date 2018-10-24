#!/usr/bin/env python
#coding=utf-8

# Created by zhaohongwei on 2016-11-03
# Blog: http://blog.csdn.net/z_johnny

import os

class HwCleanPyc(object):
    def __init__(self,pyc_path = os.getcwd()):
        self.pyc_path = pyc_path

    def cleanPyc(self):
        ''' Auto create .pyc and del it '''
        # Del all pyc in the current directory
        for pycpath, pycfolder, pycname in os.walk(self.pyc_path):
            for pyccase in pycname:
                if pyccase.endswith(".pyc"):
                    os.remove(os.path.join(pycpath, pyccase))

if __name__ == '__main__':
    pyc_path = os.getcwd()
    HwClean = HwCleanPyc(pyc_path)
    HwClean.cleanPyc()
