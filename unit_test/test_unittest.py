#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest


class Test(unittest.TestCase):
    # def setUp(self):
    #     print('start')
    @classmethod
    def setUpClass(cls):
        print("start")

    def test_1(self):
        print(1)

    def test_2(self):
        print(2)

    def test_3(self):
        print(3)

    # def tearDown(self):
    #     print('end')

    @classmethod
    def tearDownClass(cls):
        print("end")


if __name__ == "__main__":
    unittest.main()
