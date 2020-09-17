import main
import unittest
import jieba
import logging
import os
import sys

os.chdir(sys.path[0])


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        jieba.setLogLevel(logging.INFO)

    def tearDown(self) -> None:
        print("end!")

    def test_add(self):
        with open("sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            source = fp.read()
        with open("sim_0.8/orig_0.8_add.txt", "r", encoding='UTF-8') as fp:
            target = fp.read()
        sim = round(main.jaccrad(source, target), 2)
        print("测试样本：orig_0.8_add.txt ,相似度为： ","%.2f" %sim)

    def test_del(self):
        with open("sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            source = fp.read()
        with open("sim_0.8/orig_0.8_del.txt", "r", encoding='UTF-8') as fp:
            target = fp.read()
        sim = round(main.jaccrad(source, target), 2)
        print("测试样本：orig_0.8_del.txt ,相似度为： ","%.2f" %sim)

    def test_dis_1(self):
        with open("sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            source = fp.read()
        with open("sim_0.8/orig_0.8_dis_1.txt", "r", encoding='UTF-8') as fp:
            target = fp.read()
        sim = round(main.jaccrad(source, target), 2)
        print("测试样本：orig_0.8_dis_1.txt ,相似度为： ","%.2f" %sim)

    def test_dis_3(self):
        with open("sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            source = fp.read()
        with open("sim_0.8/orig_0.8_dis_3.txt", "r", encoding='UTF-8') as fp:
            target = fp.read()
        sim = round(main.jaccrad(source, target), 2)
        print("测试样本：orig_0.8_dis_3.txt ,相似度为： ","%.2f" %sim)

    def test_dis_7(self):
        with open("sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            source = fp.read()
        with open("sim_0.8/orig_0.8_dis_7.txt", "r", encoding='UTF-8') as fp:
            target = fp.read()
        sim = round(main.jaccrad(source, target), 2)
        print("测试样本：orig_0.8_dis_7.txt ,相似度为： ","%.2f" %sim)

    def test_dis_10(self):
        with open("sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            source = fp.read()
        with open("sim_0.8/orig_0.8_dis_10.txt", "r", encoding='UTF-8') as fp:
            target = fp.read()
        sim = round(main.jaccrad(source, target), 2)
        print("测试样本：orig_0.8_dis_10.txt ,相似度为： ","%.2f" %sim)

    def test_dis_15(self):
        with open("sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            source = fp.read()
        with open("sim_0.8/orig_0.8_dis_15.txt", "r", encoding='UTF-8') as fp:
            target = fp.read()
        sim = round(main.jaccrad(source, target), 2)
        print("测试样本：orig_0.8_dis_15.txt ,相似度为： ","%.2f" %sim)

    def test_mix(self):
        with open("sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            source = fp.read()
        with open("sim_0.8/orig_0.8_mix.txt", "r", encoding='UTF-8') as fp:
            target = fp.read()
        sim = round(main.jaccrad(source, target), 2)
        print("测试样本：orig_0.8_mix.txt ,相似度为： ","%.2f" %sim)

    def test_rep(self):
        with open("sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            source = fp.read()
        with open("sim_0.8/orig_0.8_rep.txt", "r", encoding='UTF-8') as fp:
            target = fp.read()
        sim = round(main.jaccrad(source, target), 2)
        print("测试样本：orig_0.8_rep.txt ,相似度为： ","%.2f" %sim)

    def testmy1(self):
        with open("sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            source = fp.read()
        with open("mytest_1.txt", "r", encoding='UTF-8') as fp:
            target = fp.read()
        sim = round(main.jaccrad(source, target), 2)
        print("测试样本：mytest_1.txt ,相似度为： ","%.2f" %sim)

    def testmy2(self):
        with open("sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            source = fp.read()
        with open("mytest_2.txt", "r", encoding='UTF-8') as fp:
            target = fp.read()
        sim = round(main.jaccrad(source, target), 2)
        print("测试样本：mytest_2.txt ,相似度为： ","%.2f" %sim)


if __name__ == '__main__':
    unittest.main()
