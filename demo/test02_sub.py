import unittest
import time


class TestSub(unittest.TestCase):

    def test01(self):
        print("test01")

    def test02(self):
        time.sleep(1)
        print("test02")
