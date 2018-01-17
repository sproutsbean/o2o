# coding:utf-8
import unittest
import os
from com.ea.common import HTMLTestRunner
from com.ea.resource import globalparameter as gl

case_path = gl.test_case_path
report_path = gl.report_path
report_file = report_path + "report.html"

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
    fr = open(report_file, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fr, title=u"o2o自动化测试报告", description=u"o2o自动化测试用例运行结果如下:",
                                           verbosity=3)
    runner.run(suite)
