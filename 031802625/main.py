import jieba
from jieba import analyse
import sys


def stopword(sentence):
    #字符串替换去标点符号
    words='的地得[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+，。！？“”《》：、． '
    for i in words:
        sentence=sentence.replace(i,'')
    return sentence 

# 计算jaccard系数
def jaccrad(essay_source, essay_target):  # essay_source为源文本，essay_target为待比较文本
    essay_source = stopword(essay_source)
    essay_target = stopword(essay_target)
    cut1 = [i for i in jieba.cut(essay_source, cut_all=True) if i != '']  # 用Jieba默认精准模式分词
    cut2 = [i for i in jieba.cut(essay_target, cut_all=True) if i != '']
    k1 = int(len(cut1)/5)
    k2 = int(len(cut2)/5)
    # 按出现次数前k个取出关键词
    keywords1 = jieba.analyse.extract_tags(",".join(cut1), topK=k1, withWeight=False)
    keywords2 = jieba.analyse.extract_tags(",".join(cut2), topK=k2, withWeight=False)
    temp = 0
    for i in keywords2:
        if i in keywords1:
            temp += 1
    # 并集
    jaccard_union = len(keywords1) + len(keywords2) - temp
    # 交集
    jaccard_index = float(temp/jaccard_union)
    # 返回杰卡德系数
    return jaccard_index


if __name__ == '__main__':

    try:
        # 从命令行读入文件
        with open(sys.argv[1], "r", encoding='UTF-8') as fp:
            source = fp.read()
        with open(sys.argv[2], "r", encoding='UTF-8') as fp:
            target = fp.read()
        sim = round(jaccrad(source, target), 2)
    except Exception as err:
        print(err)
    # 计算相似度并保留两位小数
    
    try:
        with open(sys.argv[3], "w+", encoding='UTF-8') as fp:
            fp.write(str(sim))
            # 写入输出文本
    except Exception as err:
        print(err)
