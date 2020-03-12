<head>
    <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
    <script type="text/x-mathjax-config">
        MathJax.Hub.Config({
            tex2jax: {
            skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
            inlineMath: [['$','$']]
            }
        });
    </script>
</head>

Thinking1	什么是近似最近邻查找，常用的方法有哪些    
当处理大规模数据时，精确查找的最近邻查找方法的时间成本太大，近似最近领检索（ANN）可以在牺牲可接受范围内的精度的情况下提高检索效率。ANN通过将相似数据放到同一个bucket，检索时只查找同一个bucket的数据，大幅提升检索效率。    
常用的ANN方法有：1、局部敏感哈希（LSH) 2、矢量量化（PQ)    
    
Thinking2	为什么两个集合的minhash值相同的概率等于这两个集合的Jaccard相似度    
两个集合对应的每行minhash有三种情况，A、两列的值都是1。B、一个为1，一个为0。C、两列的值都是0。C对结果无影响，因此两个集合minhash相等的概率为A/(A+B)=Jaccard相似度公式-两个集合的交集/并集    
    
Thinking3	SimHash在计算文档相似度的作用是怎样的？    
首先设置SImHash的位数并初始化；然后使用如N-Shingles的方法提取文本中的特征，使用传统hash函数计算各特征的hashcode；对hashcode的每一位进行权重加减（为1则加，否则减），计算出所设置位数的SimHash，每位大于1则为1，否则为0。    
通过SimHash算法计算出每篇文档的指纹后，将文档指纹两两对比得出汉明距离，若汉明距离小于阈值则认为两个文档相似。    
    
Thinking4	为什么YouTube采用期望观看时间作为评估指标    
CTR指标对视频搜索有一定的欺骗性，Youtube的商业模式依靠用户观看时长来投放广告获取收益，用期望观看时间作为评估指标能直观的体现视频收益。    
    
Thinking5	为什么YouTube在排序阶段没有采用经典的LR（逻辑回归）当作输出层，而是采用了Weighted Logistic Regression？    
经典的LR只有0，1两种标签，而观看时长则是连续数据，WLR引入观看时间的odds为$ \frac {\sum_{i=1}^{}[T_i}{N - k} $     
    