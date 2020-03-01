import jieba
from utils import files_processing
from gensim.models import word2vec
import multiprocessing


# 源文件目录
source_folder = './three_kingdoms/source'
segment_folder = './three_kingdoms/segment'

# 分割字词
def segment_lines(file_list, segment_out_dir, stop_words=[]):
    for i, file in enumerate(file_list):
        segment_out_name = segment_out_dir + '/segment_{}.txt'.format(i)
        with open(file, 'rb') as f:
            text = f.read()
            text_cut = jieba.cut(text)
            sentence_segment = []
            for word in text_cut:
                if word not in stop_words:
                    sentence_segment.append(word)
            result = ' '.join(sentence_segment)
            result = result.encode('utf-8')
            with open(segment_out_name, 'wb') as f1:
                f1.write(result)


# 对源文件进行分词并保存
file_list = files_processing.get_files_list(source_folder, postfix='*.txt')
segment_lines(file_list, segment_folder)

# 用word2vec对文本进行word embedding
# 若有多个文件，可用PathLineSentences
sentences = word2vec.PathLineSentences(segment_folder)
# 设置参数并训练
model = word2vec.Word2Vec(sentences, size=100, window=3, min_count=1)
print("和'曹操'最相近的词：", model.wv.most_similar(positive=['曹操']))
print("'曹操' + '刘备' - '张飞' =", model.wv.most_similar(positive=['曹操', '刘备'], negative=['张飞']))
# 更换参数
model2 = word2vec.Word2Vec(sentences, size=128, window=5, min_count=5, workers=multiprocessing.cpu_count())
print("和'曹操'最相近的词：", model2.wv.most_similar(positive=['曹操']))
print("'曹操' + '刘备' - '张飞' =", model2.wv.most_similar(positive=['曹操', '刘备'], negative=['张飞']))
