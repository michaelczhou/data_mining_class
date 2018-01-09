# coding=utf-8

import jieba
txt = "香子对米泽说"
cut_txt = " / ".join(jieba.cut(txt))
print(cut_txt)