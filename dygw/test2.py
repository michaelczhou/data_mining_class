import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from gensim.models import word2vec
from sklearn import preprocessing,decomposition
from mpl_toolkits.mplot3d import Axes3D
import os
import re
import gensim
import jieba

def find_words_nn(words):
    print('与%s相近的人物'%words[0])
    n = 0
    for k, s in model.most_similar(positive=words, topn=100):
        if k in all_names and n <5:
            print (k, s)
            n += 1


def find_relationship(a, b, c, novelname):
    """
    返回 d
    a与b的关系，跟c与d的关系一样
    """
    for k,s in model.most_similar(positive=[c, b], negative=[a], topn=100):
        if k in novel_names[novelname]:
            print("给定“{}”与“{}”，“{}”和“{}”有类似的关系".format(a, b, c, k))
def get_similarity_mat():
    '''

    :return:the matrix of similarity
    '''
    #load the model that saved before
    #model = word2vec.Word2Vec.load("./word2vec2.txt")
    model = gensim.models.Word2Vec.load('word2vec2.model')
    #read name_list
    names = open('./attrs/names.txt')
    name_list = []
    for name in names:
        name_list.append(name[:-1])

    #compute similarity matrix
    name_similarity_array = []
    for name_row in name_list:
        tmp = []
        for name_column in name_list:
             sim = model.similarity(name_row,name_column)
             tmp.append(sim)
        name_similarity_array.append(tmp)
    #normalize
    name_mat = preprocessing.MinMaxScaler().fit_transform(np.mat(name_similarity_array))
    return name_mat,name_list

def save_similar_mat(name_mat,name_list):
    '''
    save matrix
    :param name_mat:
    :param name_list:
    :return:
    '''
    f = open('./human_similar_vector.csv','w')
    for i in range(len(name_list)+1):
        for j in range(len(name_list)+1):
            if i==0 and j==0:
                f.write(' ')
            elif i == 0 and j > 0:
                f.write(name_list[j-1])
            elif i>0 and j == 0:
                f.write(name_list[i-1])
            elif i>0 and j >0:
                f.write(str(name_mat[i-1,j-1]))
            if j == len(name_list):
                f.write('\n')
            else:f.write(',')

def visualize(name_mat,name_list):
    #pcva
    # pca = decomposition.PCA(n_components=3)
    # pca.fit(name_mat)
    # U = pca.transform(name_mat)
    #svd
    U,S,V = np.linalg.svd(name_mat)

    #draw 3D picture
    ax = Axes3D(plt.figure())
    for i in range(len(name_list)):
        ax.scatter(U[i, 0], U[i, 1],U[i,2])
        ax.text(U[i, 0], U[i, 1],U[i,2],name_list[i])
    plt.show()



def visualize2(name_mat,name_list,name,layer = 2,accurate = 0.9):
    '''

    :param name_mat:
    :param name_list:
    :param name: the center of the graph
    :param layer: decide the layer number of the graph
    :param accurate: the similarity between the center with next layer
    :return:
    '''
    graph = nx.Graph()
    add_element(graph,name_mat,name_list,name,layer,accurate)
    nx.draw(graph, node_size=100, node_color='g', with_labels=True,
            font_size =8,alpha = 0.5,font_color='b',edge_color = 'gray')
    plt.show()

def add_element(graph,name_mat,name_list,name,layer,accurate):
    '''
    add element to the graph,including node and edge

    :param graph:
    :param name_mat:
    :param name_list:
    :param name:
    :param layer:
    :param accurate:
    :return:
    '''
    graph.add_node(name)
    if layer == 1:return
    pos = name_list.index(name)
    for i in range(len(name_list)):
        if name_mat[pos, i] >= accurate:
            graph.add_node(name_list[i])
            graph.add_edge(name, name_list[i])
            add_element(graph,name_mat,name_list,name_list[i],layer-1,accurate)
def get_attr(attr):
    with open('attrs/%s.txt' % attr) as f:
        # 去掉结尾的换行符
        data = [line.strip() for line in f.readlines()]

    novels = data[::2]
    attrs = data[1::2]
    all_attrs = []
    novel_attrs = {k: v.split() for k, v in zip(novels, attrs)}
    for attr in attrs:
        all_attrs.extend(attr.split())
    return novel_attrs, all_attrs

novel_names,all_names = get_attr('names')
file_names = os.listdir('./txt')
file_names = [x.strip('.txt') for x in file_names]
cuts_dir = './cuts'

wordlist = []
with open('./wordslist.txt') as f:
    for line in f:
        word = line.split()[0]
        wordlist.append(word)
    for word in list(set(wordlist)):
        jieba.add_word(word)

sentences = []

for novel in file_names:
    print ("处理：{}".format(novel))
    if os.path.exists('recut/{}.txt'.format(novel)):
        with open('recut/{}.txt'.format(novel),'r') as f2:
            text = f2.read()
            words = re.findall('[\u4E00-\u9FA5]{1,}',text)
            if len(words) > 0:
                sentences.append(words)
        continue
    with open('txt/{}.txt'.format(novel), encoding='GBK') as f:
        data = [line.strip() for line in f.readlines() if line.strip()]
    with open('recut/{}.txt'.format(novel),'w') as f2:
        for line in data:
            cuts = jieba.cut(line)
            text = '/'.join(cuts)

            words = re.findall('[\u4E00-\u9FA5]{1,}',text)
            f2.write('/'.join(words)+'/')
            if len(words) > 0:
                sentences.append(words)

model = gensim.models.Word2Vec(
    sentences, size=300, window=5, min_count=20, workers=8)
model.save('word2vec2.model')
name_mat,name_list = get_similarity_mat()
save_similar_mat(name_mat,name_list)
visualize(name_mat,name_list)
visualize2(name_mat,name_list,'雪穗',3,0.9)
