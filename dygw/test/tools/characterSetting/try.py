# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

from jpype import *

# startJVM(getDefaultJVMPath(), "-Djava.class.path=C:/Users/liang/PycharmProjects/test/app/hanlp-portable-1.5.3.jar")

startJVM(getDefaultJVMPath(), "-Djava.class.path=../../app/hanlp-1.5.3.jar;../../app")

HanLP = JClass('com.hankcs.hanlp.HanLP')

# 识别日本名称
segment = HanLP.newSegment().enableJapaneseNameRecognize(1)
document = "Makoto微微一笑，摊开时刻表，让Naoko看了看。"
a = segment.seg2sentence(document).toString()
print(a)

