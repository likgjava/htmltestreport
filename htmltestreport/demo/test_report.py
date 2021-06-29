# 导包
import unittest

from htmltestreport.demo.test01_add import TestAdd
from htmltestreport.demo.test02_sub import TestSub
from htmltestreport import HTMLTestReport



# 创建测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestAdd))
suite.addTest(unittest.makeSuite(TestSub))

# 设置测试报告文件路径
report_path = "report.html"

# 实例化HTMLTestReport对象
d = "接口自动化测试报告，覆盖了项目的核心业务功能..."
runner = HTMLTestReport(report_path, title="TPshop接口自动化测试报告", description=d)

# 执行测试套件
runner.run(suite)
