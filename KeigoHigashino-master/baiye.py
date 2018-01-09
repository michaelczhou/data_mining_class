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

with open("./txt/白夜行.txt",encoding='GBK') as s:
    texts = s.read()
    ju = texts.split('。')
    len__ju = [len(s) for s in ju]
    print(len__ju)
    str1 = ','.join(str(e) for e in len__ju)
    print(type(str1))
    #out4 = "每句的长度" + str1

    num_bins = len(len__ju)
    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(len__ju, len(len__ju), normed=10)

    # ax.plot(bins, y, '--')
    ax.set_xlabel(r"白夜行")
    ax.set_ylabel(r'每句字数')
    ax.set_title(r'句子长短统计')
    fig.tight_layout()
    plt.show()