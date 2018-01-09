from jpype import *
import os
import re
from collections import Counter
startJVM('/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/amd64/server/libjvm.so', "-Djava.class.path=/home/zc/project/data_mining_class/KeigoHigashino-master/lib/hanlp-1.5.3-release/hanlp-1.5.3.jar:/home/zc/project/data_mining_class/KeigoHigashino-master/lib/hanlp-1.5.3-release/")

HanLP = JClass('com.hankcs.hanlp.HanLP')
segmentor = HanLP.newSegment().enableJapaneseNameRecognize(True)

def tj_words(filename, in_dir='./txt', out_dir=' '):
    with open(os.path.join(in_dir, '%s.txt' % filename), encoding='GBK') as f:
        print("处理：%s" %filename)

        texts = f.read()

        tj = HanLP.parseDependency(texts).toString()
        with open(os.path.join(out_dir, '%s.txt' % filename), 'w') as tcut:
            tcut.write(tj)

file_names = os.listdir('./txt')
file_names = [x.strip('.txt') for x in file_names]
out_dir = './tongji'

# for file_name in file_names :
#     tj_words(file_name,in_dir='./txt',out_dir = './tongji')

with open("./txt/以眨眼干杯.txt",encoding='GBK') as s:
    texts = s.read()
    #print(texts)
    ju = texts.split('。')
    print(len(ju))
    for list in ju:
        print(len(list))
    len__ju = [len(s) for s in ju]
    print(type(len__ju))
    print(len__ju)
    print(ju)
    wen = texts.split('？')
    print(len(wen))
    tan = texts.split('！')
    print(len(tan))

    ss = HanLP.extractSummary(texts, 100)
    #HanLP.parseDependency(ss)
    print(ss)
    str1 = ''.join(ss)
    t = HanLP.parseDependency(str1)
    print(t)
    print(type(t))
    #t.to_conll(style=4)
    #with open('./tongji/以眨眼干杯.txt', 'w') as fcut:
        #fcut.write(str)
    #print(HanLP.parseDependency(texts))