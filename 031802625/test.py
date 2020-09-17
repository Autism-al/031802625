import calculate
import unittest
import jieba
import logging
import os
import sys
import coverage
os.chdir(sys.path[0])


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        jieba.setLogLevel(logging.INFO)

    def tearDown(self) -> None:
        print("end!")

    def test_case(self):

        example_txt = [
            'sim_0.8/orig_0.8_add.txt',
            'sim_0.8/orig_0.8_del.txt',
            'sim_0.8/orig_0.8_dis_1.txt',
            'sim_0.8/orig_0.8_dis_3.txt',
            'sim_0.8/orig_0.8_dis_7.txt',
            'sim_0.8/orig_0.8_dis_10.txt',
            'sim_0.8/orig_0.8_dis_15.txt',
            'sim_0.8/orig_0.8_mix.txt',
            'sim_0.8/orig_0.8_rep.txt',
            'mytest_1.txt',
            'mytest_2.txt']

        txts = [
            'orig_0.8_add.txt',
            'orig_0.8_del.txt',
            'orig_0.8_dis_1.txt',
            'orig_0.8_dis_3.txt',
            'orig_0.8_dis_7.txt',
            'orig_0.8_dis_10.txt',
            'orig_0.8_dis_15.txt',
            'orig_0.8_mix.txt',
            'orig_0.8_rep.txt',
            'mytest_1.txt',
            'mytest_2.txt']

        with open('sim_0.8/orig.txt', "r", encoding='UTF-8') as fp:
            s1 = fp.read()

        for i in range(11):
            with open(example_txt[i], "r", encoding='UTF-8') as fp:
                s2 = fp.read()
            ans = round(calculate.Jaccrad(s1, s2), 2)
            print('测试样本：{} , 相似度：{}'.format(txts[i], ans))
            i += 1


if __name__ == '__main__':
    unittest.main()
