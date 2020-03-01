import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from deepctr.models import DeepFM
from deepctr.inputs import SparseFeat, get_feature_names
import time
import datetime


# sample数据集
print('-'*20 + 'MovieLens_sample数据集' + '-'*20)
# 加载数据
data = pd.read_csv('movielens_sample.txt')
# 稀疏特征和目标
sparse_features = ['user_id', 'movie_id', 'gender', 'age', 'occupation', 'zip', 'timestamp']
target = ['rating']


# 将timestamp转换为与样本最早时间的月份差
def timestamp2time(timestamp):
    time_array = time.localtime(timestamp)
    otherstyletime = time.strftime("%Y-%m", time_array)
    return otherstyletime


def time_minus_min(r_time):
    d = datetime.datetime.strptime(r_time, '%Y-%m')
    months = (d.year - min_time.year) * 12 + (d.month - min_time.month)
    return months


# 样本中的最早年月
min_time = datetime.datetime.strptime(time.strftime('%Y-%m', time.localtime(data['timestamp'].min())), '%Y-%m')

data['timestamp'] = data['timestamp'].apply(timestamp2time)
data['timestamp'] = data['timestamp'].apply(time_minus_min)

# 对特征标签进行编码
for feature in sparse_features:
    lbenc = LabelEncoder()
    data[feature] = lbenc.fit_transform(data[feature])

# 计算每个特征中不同特征值的数量
fixlen_feature_columns = [SparseFeat(feature, data[feature].nunique()) for feature in sparse_features]
linear_feature_columns = fixlen_feature_columns
dnn_feature_columns = fixlen_feature_columns
feature_names = get_feature_names(linear_feature_columns + dnn_feature_columns)

# 分割数据集为训练集和测试集
train, test = train_test_split(data, test_size=0.2)
train_model_input = {name: train[name].values for name in feature_names}
test_model_input = {name: test[name].values for name in feature_names}

# 用DeepFm进行训练
model = DeepFM(linear_feature_columns, dnn_feature_columns, task='regression')
model.compile('adam', 'mse', metrics=['mse'], )
history = model.fit(train_model_input, train[target].values, batch_size=256, epochs=1, verbose=True, validation_split=0.2, )

# 预测
pred_ans = model.predict(test_model_input, batch_size=256)
#输出RMSE或MSE
mse = round(mean_squared_error(test[target].values, pred_ans), 4)
rmse = mse ** 0.5
print('test RMSE', rmse)
print('-'*30)
print('-'*30)
################################################
# 完整 MovieLens 数据集

print('-'*20 + '完整 MovieLens 数据集' + '-'*20)
# 加载数据
data = pd.read_csv('ratings.csv')
# 稀疏特征和目标
sparse_features = ['userId', 'movieId', 'timestamp']
target = ['rating']

# 样本中的最早年月
min_time = datetime.datetime.strptime(time.strftime('%Y-%m', time.localtime(data['timestamp'].min())), '%Y-%m')

# 将timestamp转换为与样本最早时间的月份差
data['timestamp'] = data['timestamp'].apply(timestamp2time)
data['timestamp'] = data['timestamp'].apply(time_minus_min)

# 对特征标签进行编码
for feature in sparse_features:
    lbenc = LabelEncoder()
    data[feature] = lbenc.fit_transform(data[feature])

# 计算每个特征中不同特征值的数量
fixlen_feature_columns = [SparseFeat(feature, data[feature].nunique()) for feature in sparse_features]
linear_feature_columns = fixlen_feature_columns
dnn_feature_columns = fixlen_feature_columns
feature_names = get_feature_names(linear_feature_columns + dnn_feature_columns)

# 分割数据集为训练集和测试集
train, test = train_test_split(data, test_size=0.2)
train_model_input = {name: train[name].values for name in feature_names}
test_model_input = {name: test[name].values for name in feature_names}

# 用DeepFm进行训练
model = DeepFM(linear_feature_columns, dnn_feature_columns, task='regression')
model.compile('adam', 'mse', metrics=['mse'], )
history = model.fit(train_model_input, train[target].values, batch_size=256, epochs=1, verbose=True, validation_split=0.2, )

# 预测
pred_ans = model.predict(test_model_input, batch_size=256)
#输出RMSE或MSE
mse = round(mean_squared_error(test[target].values, pred_ans), 4)
rmse = mse ** 0.5
print('test RMSE', rmse)