Thinking1	CTR数据中的类别数据处理，编码方式有哪些，区别是什么     
Label Encoder：将类别特征转化为1，2，3，4...等的整数，不改变特征列的数量。   
OneHot Encoder：将类别特征的每种类别生成新的列，以0，1表示。        
    
Thinking2	对于时间类型数据，处理方法有哪些        
使用DataFrame，用to_datetime函数将时间类型数据转化为datetime类型；     
在read_csv()方法中，通过设置parse_dates参数直接将时间类型数据转换成DatetimeIndex;        
            
Thinking3	你是如何理解CTR预估中的特征组合的，请举例说明    
将不同特征进行交叉组合获得新的特征，例如将年龄和性别交叉，其中的年龄小性别女的样本组合成新特征中的类别'少女'。
    
Thinking4：	DCN和xDeepFM都可以进行自动特征组合，有何区别     
DCN的Cross层接在Embedding层之后，以bit-wise的方式进行自动特征组合，意识不到Field vector的概念；      
异于DCN的cross以嵌入向量中的单个bit为最细密度，xDeepFM将FM的vector-wise思想引入到Cross部分。    
        
Thinking5：	今天讲解的特征组合只是特征工程中的一部分，你理解的特征工程都包括哪些，不防做个思维导图     
特征使用方案：基于业务理解，找出可能对因变量有影响的所有自变量，评估可用性；      
特征获取方案：设定通过什么渠道获取这些特征，特征存储；     
特征处理：特征清洗，数据预处理；        
特征监控：特征重要性分析，监控重要特征。
