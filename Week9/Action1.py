import re
from datasketch import MinHash, MinHashLSHForest
import jieba.posseg


# 加载数据
f = open('weibos.txt', 'r', encoding='utf-8')
# sentences = re.split('[…。？！]', f.read().replace('\n', ''))
sentences = []
for line in f.readlines():
    sentences += re.split('[…。？！]', line.replace('\n', ''))


# 使用jieba进行分词
def get_item_str(text):
    item_str = ''
    item = (jieba.posseg.cut(text))
    for i in list(item):
        if i.word not in list(stop):
            item_str += (i.word + ' ')
    return item_str


# 创建MinHash
def get_minhash(item_str):
    temp = MinHash()
    for d in item_str:
        temp.update(d.encode('utf-8'))
    return temp


# 停用词
stop = ''
# 获得分词后的documents
documents = []
for text in sentences:
    temp = get_item_str(text)
    documents.append(temp)

# 创建LSH Forest及MinHash对象
minhash_list = []
forest = MinHashLSHForest()
for i in range(len(documents)):
    temp = get_minhash(documents[i])
    minhash_list.append(temp)
    forest.add(i, temp)
# 为进行检索index所有key
forest.index()
# 查询并输出结果
query = '国足输给叙利亚后，里皮坐不住了，直接辞职了'
minhash_query = get_minhash(get_item_str(query))
result = forest.query(minhash_query, 3)
for i in range(len(result)):
    print(result[i], minhash_query.jaccard(minhash_list[result[i]]), documents[result[i]])
print('Top-3 Neighbours: ', result)
