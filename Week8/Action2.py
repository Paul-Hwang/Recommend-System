from surprise import Dataset, Reader, KNNBaseline, accuracy
from surprise.model_selection import KFold


# 读取数据
reader = Reader(line_format='user item rating timestamp', sep=',', skip_lines=1)
data = Dataset.load_from_file('ratings.csv', reader=reader)

sim_options = {'user_based': True, 'name': 'pearson_baseline'}
algo = KNNBaseline(sim_options=sim_options)
# K折交叉验证
kf = KFold(n_splits=3)
for train, test in kf.split(data):
    # 训练并预测
    algo.fit(train)
    pred = algo.test(test)
    accuracy.rmse(pred, verbose=True)
    accuracy.mae(pred, verbose=True)
