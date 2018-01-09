# coding=utf-8

'''
此部分工作得到每篇文章中的日文名称以及其出现的次数和位置
方法是通过hanLP的日文分词获取日文名称，位置为目前出现在文章中的行数
'''

# 修改默认编码格式
import sys
import os

reload(sys)
sys.setdefaultencoding('gbk')

from jpype import *

startJVM(getDefaultJVMPath(),
         "-Djava.class.path=C:/Users/liang/PycharmProjects/test/app/hanlp-1.5.3.jar;C:/Users/liang/PycharmProjects/test/app")
HanLP = JClass('com.hankcs.hanlp.HanLP')
# 识别日本名称
segment = HanLP.newSegment().enableJapaneseNameRecognize(1)

names = {}


def find_name(file_name, prefix_dir, output_dir):
    originalDir = "../../keywordresult/originalName/"
    filteredDir = "../../keywordresult/filteredName/"
    originalName = open(originalDir + file_name, "w+")
    filteredName = open(filteredDir + file_name, "w+")

    with open((prefix_dir + "/" + file_name)) as source_text:
        print("开始处理: " + str(file_name).encode("utf-8"))
        lines = source_text.readlines()
        for i in range(len(lines)):
            eachline = lines[i]
            seg_txt = segment.seg(eachline)
            for each_word in seg_txt:
                # 出现了日本名字
                if ("nrj" in str(each_word)):
                    # print(str(each_word).encode("utf-8"))
                    # print(i + 1)
                    name = str(each_word).encode("utf-8")
                    if not names.has_key(name):
                        originalName.writelines(str(each_word).encode("utf-8") + '\n')
                        originalName.writelines(str(i + 1) + '\n')
                        names[name] = 1
                    else:
                        names[name] += 1
                # if ("nx" in str(each_word)):
                #     # print(str(each_word).encode("utf-8"))
                #     # print(i + 1)
                #     name = str(each_word).encode("utf-8")
                #     if not names.has_key(name):
                #         originalName.writelines(str(each_word).encode("utf-8") + '\n')
                #         originalName.writelines(str(i + 1) + '\n')
                #         names[name] = 1
                #     else:
                #         names[name] += 1
        for key in names:
            if (names.get(key) > 5) or (("nrjb" not in key) and names.get(key) > 1):
                filteredName.writelines(str(key) + " " + str(names.get(key)) + '\n')
        source_text.close()


file_name_list = os.listdir('../../txt')

for file_name in file_name_list:
    find_name(file_name, "../../txt", "../name_result/")
# file_name = file_name_list[1]
# find_name(file_name, "../../txt", "../name_result/")
