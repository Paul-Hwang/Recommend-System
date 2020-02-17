#**Reading Summary of ** Slope One Predictors for Online Rating-Based Collaborative Filtering    
##### By Daniel Lemire & Anna Maclachlan    
    
###Summary:     
这篇文章介绍了三种对物品评分两两相比较得出平均差的基于模型的slope one算法。    
此文目的目的不是去比较slope one算法和其他协同过滤算法的准确率, 而是通过对比介绍slope one算法的5个优点：    
1. 这是一种可以简单实现和维护的算法。    
2. 这种算法可以即刻更新预测。    
3. 在查询时有效，节省存储空间。    
4. 对新用户推荐时减少对新用户的信息依赖。    
5. 在不牺牲易用性和扩展性的前提保持准确率。    
    
Slope One算法相较于基于内存的算法和其他基于模型的算法是有竞争力的。    
基于内存的算法依赖用户之间的相似性， 因此不能对在线查询预计算；此外，基于内存的算法需要至少一定数量的用户与评分。    
相较于memory-based算法，model-based的算法可以快速响应查询，但有更高的学习和更新成本。当查询速度很重要时，model-based算法是更优选。
    
这篇文章选择了memory-based的Pearson算法，model-based的三种baseline schemes（Per User Average, Bias From Mean, Adjusted Cosine Item-Based)与三种Slope one算法的平均误差(MAE，越小越好)对比，得出不错的结果：在EachMovie数据集中，Bi-Polar Slope One算法和Pearson算法效果最好，而在Movielens数据集中三种Slope One算法皆得出几种算法中最低的MAE。    
此文得出结论：Slope One算法是一种简单有效的且准确率能与其他model-based算法和memory-based算法相比较的算法。    
    
###Thinking:    
算法不一定是越复杂的效果越好，有时候简单易用的算法也能达到相近的效果。当需求对时间要求较为紧迫时，运行简单且能得到相当准确率的算法是更优选。
根据需求决定使用什么算法，不一定要一味地追求准确率，也要考虑易用性和扩展性，时间复杂度等其他因素。    