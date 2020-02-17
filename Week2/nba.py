import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# 加载数据
data = pd.read_csv('D:\\GitHub\\Recommend-System\\Lesson 2 Homework\\NBA_Players.csv')
# 清除列名的空格
data.columns = list(i.strip() for i in data.columns.to_list())
# 去掉'URL'列
data.drop('URL', axis=1, inplace=True)
# 将值为'-'或'Not signed'的数据改成空值
data[data.isin(['-', 'Not signed'])] = np.nan
'''data['PPG_LAST_SEASON'].fillna(data['PPG_LAST_SEASON'].mean(), inplace=True)
data['APG_LAST_SEASON'].fillna(data['PPG_LAST_SEASON'].mean(), inplace=True)
data['RPG_LAST_SEASON'].fillna(data['PPG_LAST_SEASON'].mean(), inplace=True)
data['PER_LAST_SEASON'].fillna(data['PPG_LAST_SEASON'].mean(), inplace=True)'''
# 更改'AGE'列数据类型为'float64'并将空值改为0
data['AGE'] = data['AGE'].astype('float64')
data['AGE'].fillna(0, inplace=True)
# 清除'SALARY'列的值的逗号, 将空值改为0, 并更改'SALARY'列数据类型为'int'
data['SALARY'] = data['SALARY'].str.replace(',', '')
data['SALARY'].fillna(0, inplace=True)
data['SALARY'] = data['SALARY'].astype('int')

# data['COLLEGE'].fillna(data['COLLEGE'].value_counts().index[0], inplace=True)

# EXPERIENCE 饼状图
fig = plt.figure(figsize=(10, 10))  # 设置图的大小
experience_group = data['EXPERIENCE'].value_counts(bins=[0, 3, 5, 8, 10, 15, 25])  # 设置饼状图的区间
labels = ['0-3 years', '3-5 years', '5-8 years', '8-10 years', '10-15 years', 'over 15 years']  # 每个区间的标签
explodes = (0, 0, 0, 0, 0.1, 0.2)  # 饼状图的突出程度
cmap = plt.get_cmap('tab20c')  # 颜色
color = cmap(np.array([1, 2, 7, 8, 9, 12]))  # 颜色
# 画图
ax = plt.pie(experience_group, labels=labels, explode=explodes, autopct='%1.0f%%', colors=color, pctdistance=0.55, labeldistance=1.05)
# 标题
plt.title('Experience Groups of NBA players in 18-19 Season', fontsize=12)
plt.show()

# COLLEGE 柱状图
fig1 = plt.figure(figsize=(11.7, 8.27))  # 设置图的大小
ncount = len(data['COLLEGE'].value_counts())  #
order = data['COLLEGE'].value_counts().index[:15].tolist()
ax1 = sns.countplot(x='COLLEGE', data=data, order=order, palette='rainbow')  # 绘图
ax1.grid(True)  # 显示网格
ax1.set_title('Graduate College of NBA players')  # 标题
ax1.set_xlabel('College name')  # x轴标题
ax1.set_ylabel('Number of NBA players')  # y轴标题
# 在数据顶部显示百分比
for p in ax1.patches:
    x = p.get_bbox().get_points()[:, 0]
    y = p.get_bbox().get_points()[1, 1]
    ax1.annotate('{:.1f}%'.format(100.*y/ncount), (x.mean(), y), ha='center', va='bottom')
fig1.autofmt_xdate()  # x坐标轴斜着显示
# ax.set_ylim(0, 2)  设置y轴刻度范围

# 