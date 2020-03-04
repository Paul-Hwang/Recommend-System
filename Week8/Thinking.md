Thinking1	在CTR点击率预估中，使用GBDT+LR的原理是什么？    
在CTR预估中，GBDT通过对原数据特征进行特征组合产生新的特征，然后将所有特征传入LR，LR对GBDT产生的输入数据进行分类。    
    
Thinking2	Wide & Deep的模型结构是怎样的，为什么能通过具备记忆和泛化能力（memorization and generalization）    
Wide & Deep算法结合了线性模型的记忆能力和DNN模型的泛化能力，在训练过程中同时优化两个模型的参数。    
Wide推荐采用Linear Regression，可解释性强但特征需要人为设计；Deep推荐通过深度学习出可解释性差的隐性特征。两个模型分别对全量数据进行预测，然后根据权重组合最终预测结果。    
    
Thinking3	在CTR预估中，使用FM与DNN结合的方式，有哪些结合的方式，代表模型有哪些？    
使用FM与DNN结合的方式有两种，一种是并行结构，两个模型分别对全量数据进行预测并根据权重组合结果，代表模型为DeepFM。    
另一种是并行结构，将FM的结果作为DNN的输入来进行运算，代表模型为NFM。    
    
Thinking4	Surprise工具中的baseline算法原理是怎样的？BaselineOnly和KNNBaseline有什么区别？    
Baseline算法是基于一个基准来进行预测打分，每个Baseline算法的差异则在于这个基准的选择。    
BaselineOnly是基于统计的基准预测打分；    
而KNNBaseline则是协同过滤算法的变种，考虑每个用户评分的基线。    
    
Thinking5	GBDT和随机森林都是基于树的算法，它们有什么区别？    
GBDT是通过集成弱学习器来提高预测精度，一个学习器的残差为下个学习器的输入，不断缩小残差，将每个学习器的结果相加得到最终预测结果    
随机森林则通过自助采样的方法生成多个并行式的分类器，通过"少数服从多数"原则（投票）确定最终结果。    
    
Thinking6	基于邻域的协同过滤都有哪些算法，请简述原理    
KNNBasic：通过计算近邻的相似度对物品进行评分预测并排序推荐。    
KNNWithMeans：KNNBasic的变种，在计算时降均值提取出来然后计算用户兴趣时减去均值。    
KNNWithZScore：在KNNWithMeans基础上将用户兴趣计算归一化。    
KNNBaseline：在计算相似度是考虑用户打分的偏差。    