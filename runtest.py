# coding=utf-8
import unittest
import time
import HTMLTestRunner

'''运行全部测试用例第二种方法discover,这种方法比较好'''
test_dir = "D:\\workspace_python\\com\\selenium\\tueasy"
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_000create_doc.py')

if __name__ == "__main__":
    nowtime = time.strftime("%Y-%m-%d %H%M%S")
    filename = 'D:\\' + nowtime + ' TestResult.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='TuEasy_TestReport',
        description=u'图易产品测试报告'
    )
    runner.run(discover)
    fp.close()