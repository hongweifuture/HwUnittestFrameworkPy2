#!/usr/bin/env python
# coding=utf-8

# Created by zhaohongwei on 2016-11-03
# Blog: http://blog.csdn.net/z_johnny

from HwTestReportCN import HwHTMLTestReport as HwTestRunnerChinese
from HwTestReportEN import HwHTMLTestReport as HwTestRunnerEnglish
import time
import unittest
import yaml

class HwTestRunnerCN(object):
    def __init__(self, config_runner, suite):
        self.suite = suite
        with open(config_runner,'rb') as config :
            self.allConfig = yaml.load(config)

    def addReport(self):
        ''' Collect all testcase result to HTMLTestRunner'''
        report_name = self.allConfig["report"]["name"]
        localtime = str(time.strftime('%Y_%m_%d_%A_%H_%M_%S'))
        filename = './result/%s%s.html'%(report_name,localtime)

        with open(filename, 'wb') as report:
            runner = HwTestRunnerChinese(stream = report,
                                    title = self.allConfig["report"]["title"],
                                    description = self.allConfig["report"]["description"],
                                    tester = self.allConfig["report"]["tester"] )
            runner.run(self.suite)


class HwTestRunnerEN(object):
    def __init__(self, config_runner, suite):
        self.suite = suite
        with open(config_runner,'rb') as config :
            self.allConfig = yaml.load(config)

    def addReport(self):
        ''' Collect all testcase result to HTMLTestRunner'''
        report_name = self.allConfig["report"]["name"]
        localtime = str(time.strftime('%Y_%m_%d_%A_%H_%M_%S'))
        filename = './result/%s%s.html'%(report_name,localtime)

        with open(filename, 'wb') as report:
            runner = HwTestRunnerEnglish(stream = report,
                                    title = self.allConfig["report"]["title"],
                                    description = self.allConfig["report"]["description"],
                                    tester = self.allConfig["report"]["tester"] )
            runner.run(self.suite)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    cases_path = "./cases"
    config_runner = './config/configReport.yaml'
    config_logging = './config/configLOG.yaml'
    testCN = HwTestRunnerCN(cases_path,config_runner,config_logging,suite)
    testEN = HwTestRunnerEN(cases_path, config_runner, config_logging, suite)
    testCN.run()
    testEN.run()
