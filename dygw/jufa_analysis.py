from jpype import *
import os
import re
from collections import Counter
startJVM('/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/amd64/server/libjvm.so', "-Djava.class.path=/home/zc/project/data_mining_class/dygw/lib/hanlp-1.5.3-release/hanlp-1.5.3.jar:/home/zc/project/data_mining_class/dygw/lib/hanlp-1.5.3-release/")

HanLP = JClass('com.hankcs.hanlp.HanLP')
segmentor = HanLP.newSegment().enableJapaneseNameRecognize(True)


with open("./txt/以眨眼干杯.txt",encoding='GBK') as s:
    texts = s.read()
    #print(texts)
    ju = texts.split('。')
    # for list in ju:
    #     print(len(list))
    len__ju = [len(s) for s in ju]

    ss = HanLP.extractSummary(texts, 100)
    # 自动摘要
    with open('./hanlp/摘要.txt', 'w') as scut:
        scut.write(str(ss))

    str1 = ''.join(ss)

    NLPTokenizer = JClass('com.hankcs.hanlp.tokenizer.NLPTokenizer')
    # 关键词提取
    print(NLPTokenizer.segment(str1))


    t = HanLP.parseDependency(str1)
    # 依存句法分析
    with open('./hanlp/依存关系.txt', 'w') as fcut:
        fcut.write(str(t))