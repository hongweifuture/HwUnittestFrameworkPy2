# HwUnittestFrameworkPy2
python基于unittest自动化测试框架，参数化，可视化，功能封装

# 基础
[Python自动单元测试框架介绍](https://www.ibm.com/developerworks/cn/linux/l-pyunit/)

[Python单元测试框架基础](http://pyunit.sourceforge.net/pyunit_cn.html)

# 特点
1. python2语言，基于unittest
2. 由ini改为yaml文件参数化配置，实现配置与代码分离
3. 支持xlsx、csv、xml等格式数据驱动，实现数据与代码分离
4. log日志、report报告记录、生成和存储
5. 测试用例模板化，易编写
6. 自定义邮件发送测试结果
7. 支持Selenium和Request套用框架

# 目录结构
文件/文件夹 | 说明
-- | --
startup.py | 启动程序
cases | 测试用例
config | 配置文件
data | 数据驱动
driver | 驱动文件
log | 日志存放
report | 报告留存
result | 测试结果
screenshot | 过程截图
source | 封装的库类

![toc](https://github.com/hongweifuture/HwUnittestFrameworkPy2/blob/master/screenshot/toc.png)

# 使用方法
**请删除.gitignore**

## 安装python2
[python 安装教程](https://blog.csdn.net/z_johnny/article/details/50733843)

## 安装PyYaml模块
[YAML 中文文档](https://yq.aliyun.com/articles/509500)
```python
pip install PyYaml
```
## 编写用例
### 模板
框架调用测试用例，无论是手动添加suite还是discover自动识别测试用例，main都不会被调用，只是在脱离框子单独测试用例的时候会用到，模板使用为手动
```python
#!/usr/bin/python
# coding=utf-8
import unittest

class TestModule(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Photo(self):
        pass

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestModule("test_Photo"))
    unittest.TextTestRunner().run(suite)
```
### 范例
```python
#!/usr/bin/python
# coding=utf-8

# Created by zhaohongwei on 2018-10-22
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
```
## 技巧1 用例添加log，引入HwLogging
HwLogging模块打包了logging的功能，配置参数化，输出格式化，使用方法同logging
```python
#from HwLogging import HwLogging
from source.HwLogging import HwLogging

self.logging = HwLogging().outputLog()

self.logging.debug()
self.logging.info()
self.logging.warning()
self.logging.error()
self.logging.critical()
```
格式化输出
```txt
2018-10-24 10:37:11,440  - HwUnittest.py : INFO  -
2018-10-24 10:37:11,440  - HwUnittest.py : INFO  The testcase number is : 3
2018-10-24 10:37:11,440  - HwUnittest.py : INFO  The testcase name is : ANDROID.py
2018-10-24 10:37:11,440  - HwUnittest.py : INFO  The testcase name is : Jenkins.py
2018-10-24 10:37:11,440  - HwUnittest.py : INFO  The testcase name is : Web_API.py
2018-10-24 10:37:11,457  - ANDROID.py : WARNING  123456789
2018-10-24 10:37:11,457  - ANDROID.py : INFO  Test Down
2018-10-24 10:37:11,459  - ANDROID.py : WARNING  123456789
2018-10-24 10:37:11,459  - ANDROID.py : ERROR  This is error message
2018-10-24 10:37:11,459  - ANDROID.py : INFO  Test Down
2018-10-24 10:37:11,460  - ANDROID.py : WARNING  123456789
2018-10-24 10:37:11,460  - ANDROID.py : INFO  Test Down
2018-10-24 10:37:16,562  - HwCutfile.py : INFO  Has been cut the file is 目前最新版本2018_10_24_Wednesday_10_37_11.html
```

## 技巧2 输出报告文件 可选中文或者英文
使用unittest，生成html报告，由于使用在线Bootstrap，需要联网，离线模式排版不美观
```python
suite = unittest.TestSuite()

# HwStartup(suite, 'CN') , you must choose
# you must choose CN or EN,it's report language

HwStartup(suite, 'CN').startup()
#HwStartup(suite, 'EN').startup()
```
![reporten](https://github.com/hongweifuture/HwUnittestFrameworkPy2/blob/master/screenshot/reporten.png)

![reporten](https://github.com/hongweifuture/HwUnittestFrameworkPy2/blob/master/screenshot/reportcn.png)

## 技巧3 发送邮件
HwSendEmail打包smtp邮件，默认发送result文件夹附件，只需传送邮件标题和内容即可
```python
# send email , you can choose
ISOTIMEFORMAT='_%Y-%m-%d_%A'
current_time =str(time.strftime(ISOTIMEFORMAT))

email_tiltle = 'johnny test'+'%s'%current_time       # as johnny test_2016-06-20_Monday
email_content = u'本轮自动化测试完成，详情请查看附件，本邮件是程序自动发送，请勿回复！'

HwSendEmail(email_tiltle,email_content).sendemail()
```
## 技巧4 测试版本留存
可配置source和destination文件夹，对文件进行移动并留存
```python
# HwFileMove() move result to report , you can choose

HwFileMove().moveFile()
```
## 技巧5 删除pyc
调试脚本过程中会出现pyc，可选进行删除
```python
# delde pyc , you can choose
HwCleanPyc().cleanPyc()
```

# bug
没有打印信息的测试用例，html报告无法收起

# extend
1. 加入数据驱动，如excel
1. 加入截图功能
1. 加入统计图







