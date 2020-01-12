Thinking 1: 既然内容相似度计算简单，能频繁更新，为什么还需要协同过滤算法呢？  
A: 在推荐系统中, data可以是物品本身的, 也可以是基于用户行为的; 内容相似度计算只考虑了物品本身的data, 而协同过滤算法通过分析用户行为给用户推荐可能感兴    趣的物品或内容  
Thinking 2: 你需要推荐系统么？哪些情况下不需要推荐系统？  
A: 不是所有项目都需要推荐系统, 在项目初期或未成熟阶段, 与其搭建一个推荐系统, 不如着力于新增用户; 如果项目中的物品数量少到能用人工应付, 那么用户产生的连接肯定不多, 这样的项目不需要推荐系统  
Thinking 3: 如果给一个视频打标签，视频中有音乐作为背景音乐，采用了NLP方式对内容自动打标签，可能存在什么问题？  
A: NLP识别到背景音乐, 会给视频打上音乐标签, 但是视频内容可能是其他类型