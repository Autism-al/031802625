import jieba
from jieba import analyse
from jieba.finalseg import cut
import math
import sys

# 计算jaccard系数



def Jaccrad(essay_source, essay_target): # essay_source为源文本，essay_target为待比较文本
    cut1 = [i for i in jieba.cut(essay_source, cut_all=True) if i != '']# 用Jieba默认精准模式分词
    cut2 = [i for i in jieba.cut(essay_target, cut_all=True) if i != '']
    k1 = int(len(cut1)/5)
    k2 = int(len(cut2)/5)
    keywords1 = jieba.analyse.extract_tags(",".join(cut1), topK=k1, withWeight=False)#按出现次数前k个取出关键词
    keywords2 = jieba.analyse.extract_tags(",".join(cut2), topK=k2, withWeight=False)
    temp = 0
    for i in keywords2:
        if i in keywords1:
            temp += 1
    jaccard_union = len(keywords1 ) + len(keywords2) - temp #并集
    Jaccard_Index = float(temp/jaccard_union) #交集
    return Jaccard_Index #返回杰卡德系数

if __name__ == '__main__':
    #从命令行读入文件
    with open(sys.argv[1], "r", encoding='UTF-8') as fp:
        essay_source = fp.read()
    with open(sys.argv[2], "r", encoding='UTF-8') as fp:
        essay_target = fp.read()
    similarity = round(Jaccrad(essay_source, essay_target),2)
    #计算相似度并保留两位小数
    #写入输出文本
    with open(sys.argv[3], "w+", encoding='UTF-8') as fp:
        fp.write(str(similarity))

