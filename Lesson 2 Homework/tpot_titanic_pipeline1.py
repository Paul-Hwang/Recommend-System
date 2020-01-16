import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer

# 数据加载
train = pd.read_csv('./train.csv')
test = pd.read_csv('./test.csv')
# 使用平均年龄来填充年龄中的nan值
train['Age'].fillna(train['Age'].mean(), inplace=True)
test['Age'].fillna(test['Age'].mean(), inplace=True)
# 使用平均票价填充NAN值
test['Fare'].fillna(test['Fare'].mean(), inplace=True)
# 使用登录最多的港口来填充登录港口的nan值
train['Embarked'].fillna(train['Embarked'].value_counts().reset_index()['index'][0], inplace=True)
test['Embarked'].fillna(train['Embarked'].value_counts().reset_index()['index'][0], inplace=True)
# 特征选择
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
train_features = train[features]
test_features = test[features]
train_label = train['Survived']

dvec = DictVectorizer(sparse=False)
train_features = dvec.fit_transform(train_features.to_dict(orient='record'))
test_features = dvec.transform(test_features.to_dict(orient='record'))


# Average CV score on the training set was: 0.8462620048961144
exported_pipeline = GradientBoostingClassifier(learning_rate=0.1, max_depth=5, max_features=0.55, min_samples_leaf=5, min_samples_split=3, n_estimators=100, subsample=0.7000000000000001)

exported_pipeline.fit(train_features, train_label)
results = exported_pipeline.predict(test_features)
