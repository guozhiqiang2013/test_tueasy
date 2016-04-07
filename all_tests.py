# coding=utf-8

import HTMLTestRunner
import time
# 引入TuEasyTestCase包下的__init__文件
import __init__

'''运行全部测试用例第一种方法，这种方法一般'''
nowtime = time.strftime("%Y-%m-%d %H%M%S")
filename = 'D:\\PyTest\\' + nowtime + ' TestResult.html'
fp = file(filename, 'wb')

runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='TuEasy_Test_Report',
    description='Report_description'
)

try:
    runner.run(suite)
except Exception, e:
    print e