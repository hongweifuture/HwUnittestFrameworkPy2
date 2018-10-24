#!/usr/bin/env python
# coding=utf-8

# Created by zhaohongwei on 2018-10-23
# Blog: http://blog.csdn.net/z_johnny

from HwTestRunner import HwTestRunnerCN
from HwTestRunner import HwTestRunnerEN
from HwLogging import HwLogging
import unittest
import os
import sys

class HwStartup(object):
    def __init__(self,  suite, language = 'EN'):
        self.cases_suite = []
        self.config_cases_path = './cases'
        self.suite = suite
        self.config_runner =  './config/configReport.yaml'
        self.language = language

        self.logging = HwLogging().outputLog()

    def getAllCases(self):
        ''' Get all testcase '''
        cases = os.listdir(self.config_cases_path)
        self.logging.info('-')
        self.logging.info('The testcase number is : %s'%(len(cases)-1))
        for case in cases:
            # Split endswith and add to list
            if case.endswith('.py') and not case.startswith('__init__'):
                cases_list = case.split('.py')
                self.cases_suite.append(cases_list[0])
                self.logging.info('The testcase name is : %s'%case)

    def runCases(self):
        ''' Run all testcase (copy it for nose) '''
        sys.path.append(self.config_cases_path)
        for test_case in self.cases_suite:
            try:
                mod = __import__(test_case.globals(),locals(),[self.suite])
                suitefn = getattr(mod,self.suite)
                self.suite.addTest(suitefn())
            except (ImportError,AttributeError):
                self.suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test_case))
        return  self.suite

    def startup(self):
        self.getAllCases()
        suite = self.runCases()
        if self.language == 'CN':
            HwTestRunnerCN(self.config_runner,suite).addReport()
        elif self.language == 'EN':
            HwTestRunnerEN(self.config_runner, suite).addReport()
        else:
            print 'Report DecodeError,Please choose CN or EN!'
            self.logging.warning('Report DecodeError,Please choose CN or EN!')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    config_cases_path = "./cases"
    config_runner = './config/configReport.yaml'
    config_logging = './config/configLOG.yaml'
    config_file = './config/configCutFile.yaml'
    testreport = HwStartup(config_cases_path,config_logging,suite)
    testreport.startup(config_runner)