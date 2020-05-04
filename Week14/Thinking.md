Thinking1	什么是Graph Embedding，都有哪些算法模型     
Graph Embedding是一种Embedding降维技术，可以有效的挖掘图网络中的节点特征表示；     
主要方法有：图因式分解机、随机游走、深度学习；     
算法模型有：Deep Walk (Random Walk + Word2Vec), Node2Vec (在Deep Walk的基础上进行改进，可以控制BFS, DFS随机游走)，GCN（一个图数据的特征提取器）。      
    
Thinking2	如何使用Graph Embedding在推荐系统，比如NetFlix 电影推荐，请说明简要的思路    
将Netflix数据集中的user与item之间的联系用图网络表示，以user和item未节点，ratings为边，使用graph embedding算出两两之间的相似度，作出推荐。     
    
Thinking3	在交通流量预测中，如何使用Graph Embedding，请说明简要的思路   
以各个路口为节点，车流速为边，根据流速快慢确定权重，使用Graph Embedding，根据路口的相似度给出流量预测。    
Thinking4：	在文本分类中，如何使用Graph Embedding，请说明简要的思路     
以单词为node，单词与单词的共现关系为边，用图网络表示，使用GCN进行分类；
以单词、文章为node，计算单词的TF-IDF作为边的权重，用图网络表示，使用GCN进行分类。   