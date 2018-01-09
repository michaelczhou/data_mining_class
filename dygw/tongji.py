#-*- coding:utf-8 -*-
from jpype import *
import os
import re
from collections import Counter
import string
from collections import namedtuple
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import tkinter
startJVM('/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/amd64/server/libjvm.so', "-Djava.class.path=/home/zc/project/data_mining_class/KeigoHigashino-master/lib/hanlp-1.5.3-release/hanlp-1.5.3.jar:/home/zc/project/data_mining_class/KeigoHigashino-master/lib/hanlp-1.5.3-release/")
#startJVM('/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/amd64/server/libjvm.so', "path=/home/zc/project/data_mining_class/KeigoHigashino-master/lib/hanlp-1.5.3-release/hanlp-1.5.3.jar:/home/zc/project/data_mining_class/KeigoHigashino-master/lib/hanlp-1.5.3-release/")
#"""
# 利用hanlp进行分词
# 因为hanlp的分词结果对人名地名分割效果较好，而jieba分词对整体分词效果较好，因此先用hanlp分词得到一些关键属性(人名地名等)
# 对所有的小说进行分词保存在cuts. 保存的是分词的原始结果，若需要得到单词的list可以用re.findall('[\u2E80-\u9FFF]{1,}',a)
# 并用正则表达式找出每本小说的有关属性保存在filters文件夹内
#"""

# Initial hanlp
HanLP = JClass('com.hankcs.hanlp.HanLP')

def process_sentences(filename, in_dir='./txt', out_dir=' ' ):
    with open(os.path.join(in_dir, '%s.txt' % filename), encoding='GBK') as f:
        print("处理：%s" %filename)

        #count_ju = count_wen = count_tan = 0

        texts = f.read()

        x = re.findall('[。]', texts)
        print(x)
        out1 = "句号的个数 = "+str(len(x))
        y = re.findall('[?]', texts)
        print(y)
        out2 = "问号的个数 = "+str(len(y))
        z = re.findall('[!]', texts)
        print(z)
        out3 = "叹号的个数 = "+str(len(z))

        ju = texts.split('。')
        len__ju = [len(s) for s in ju]
        print (len__ju)
        str1 = ','.join(str(e) for e in len__ju)
        print(type(str1))
        out4 = "每句的长度" + str1

        num_bins = len(len__ju)
        fig,ax = plt.subplots()
        n,bins,patches = ax.hist(len__ju,len(len__ju),normed=10)


        # ax.plot(bins, y, '--')
        ax.set_xlabel(filename)
        ax.set_ylabel(r'每句字数')
        ax.set_title(r'句子长短统计')
        fig.tight_layout()
        plt.show()

        foo = '{},{},{},\n{}'.format(out1,out2,out3,out4)
        with open(os.path.join(out_dir, '%s.txt' % filename), 'w') as fcut:
              fcut.write(foo)

file_names = os.listdir('./txt')
file_names = [x.strip('.txt') for x in file_names]
out_dir = './tongji'
for file_name in file_names :
    process_sentences(file_name,in_dir='./txt',out_dir = './tongji' )