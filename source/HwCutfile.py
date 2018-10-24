#!/usr/bin/env python
# coding:utf-8

# Created by zhaohongwei on 2016-06-23
# Change yaml config file on 20181008
# Blog: http://blog.csdn.net/z_johnny

import os,shutil,time
from HwLogging import HwLogging
import yaml

class HwFileMove():
    def __init__(self):
        with open('./config/configCutFile.yaml','rb') as config:
            self.allConfig = yaml.load(config)

        self.logging = HwLogging().outputLog()

        self.sourceDir = self.allConfig['FilePath']['source']
        self.destinationDir = self.allConfig['FilePath']['destination']

    def moveFile(self):
        """
        first :create destination floder ,second :copy file and delete source floder ,thired :create source floder
        """
        for sourceFile in os.listdir(self.sourceDir):
            if sourceFile.endswith('.html') :
                sourceFileName = sourceFile.split('.html')
                current_time =str(time.strftime('-%Y-%m-%d-%A-%H_%M_%S'))

                if len(os.listdir(self.sourceDir)) > 1:
                    sourceFileNames = sourceFileName[0] + current_time + '-And_Other_File'
                    destination = os.path.join(self.destinationDir,sourceFileNames)
                    shutil.copytree(self.sourceDir,destination)
                elif len(os.listdir(self.sourceDir)) == 1:
                    sourceFileNames = sourceFileName[0] + current_time
                    destination = os.path.join(self.destinationDir,sourceFileNames)
                    shutil.copytree(self.sourceDir,destination)

                shutil.rmtree(self.sourceDir)
                sourceDirNew = os.path.join(os.getcwd(),self.sourceDir[2:])
                os.system('md {}'.format(sourceDirNew))
            self.logging.info( 'Has been cut the file is %s'%sourceFile.decode('gb18030'))

if __name__ =='__main__':
    HwFileMove().moveFile()










