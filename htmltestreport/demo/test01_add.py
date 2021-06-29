# 定义一个实现加法操作的函数，并对该函数进行测试
def add(x, y):
    return x + y


# 导包
import unittest


class TestAdd(unittest.TestCase):

    def test_add_01(self):
        """加法测试01"""
        result = add(1, 1)
        print("result1=", result)
        self.assertEqual(2, result)

    def test_add_02(self):
        """加法测试02"""
        result = add(1, 1)
        print("result2=", result)

        # 断言
        self.assertEqual(2, result)
        self.assertEqual("登录成功", "登录成功！")

    @unittest.skip("就是想跳过！")
    def test_skip(self):
        """跳过测试"""
        print("这是一个跳过测试")

    def test_error(self):
        """错误测试"""
        print("这是一个错误测试")
        a = [][2]
