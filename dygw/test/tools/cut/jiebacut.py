# coding=utf-8
import os
import jieba
import sys


def cut_words(file_name, prefix_dir, output_dir):
    with open(prefix_dir + "/" + file_name) as source_text:
        print("开始处理: " + file_name)
        txt = source_text.read()
        cut_txt = " / ".join(jieba.cut(txt))
        source_text.close()
    with open(output_dir + '/' + file_name, "w") as target_text:
        txt = cut_txt.encode("utf-8")
        print(type(txt))
        target_text.write(cut_txt.encode("utf-8"))
        print(txt.strip("/"))
        target_text.close()


file_name_list = os.listdir('../txt')

for file_name in file_name_list:
    cut_words(file_name, "../txt", "../cutresult/jieba_result")
