# Information-Retrieval-System-for-Amazon-Products
Our project for IR Intro course (2018). 

---

### 基本要求：

> 1. 系统能够为一个文本集合创建索引
> 
> 2. 系统能够根据单个词语搜索相应的文件
> 
> 3. 用户交互界面：  
>  - 让用户指定需索引的文件目录
>  - 让用户输入搜索内容
>  - 显示搜索到的文件名

### 高级功能（可选）： 



> 1. 系统支持组合查询语句，该语句包含两个或多个以“OR”或“AND”连接的单词（例 如 “movie” AND “good”、“movie” OR “TV”）。系统无需支持同时包含“AND”和“OR” 的查询语句，例如(“good” OR “bad”) AND “movie”。 
> 
> 2. 系统支持短语（包含两个或多个单词）查询，例如“good movie”。 
> 
> 3. 系统能够对搜索到的文件与查询语句之间的关联度进行分析与排序，并按照关联度排序 （降序）显示搜索到的文件。 
> 
> 4. 系统能够支持一些更高级的用户交互功能（例如：系统在显示搜索结果时除了显示文件 名外，还显示文件内容，并将被查询的词汇以特殊的方式标出）。 
> 
> 5. 系统能够让用户指定一个需排除的词汇列表，这些词汇在创建反向索引时不被检索。 
> 
> 6. 其他能够提升索引与搜索质量的功能。

### 步骤：

> - 爬取数据  
爬取amazon网站上的商品信息(名称、价格、介绍)、购买信息(购买数目、评价)等
放置在json文件中，例如：

	json
	{
		"id": "03000598",
		"name": "apple iphone x, fully unlocked 5.8", 64 gb - silver",
		"price": "$1,139.00 & free shipping",
		"information": 
		{
			"color": "silver", 
			"size": "64 gb", 
			...
		},
		...
		"link": "https://www.amazon.com/gp/product/B075QN8NDJ/ref=s9_dcacsd_dcoop_bw_c_x_1_w"
	}
> 
> - 建立数据库  
最开始可以先将json文件当作一个简单的文本数据库  
在建立索引之前对搜索文档进行预处理  
预处理建立在自己对系统的需求上，例如切分文档、美化格式、替换字符、格式转换
> 
> - 建立索引  
取得一个搜索文档，添加Field(文件名、文件内容等)
> 
> - 搜索  
搜索关键字和搜索类型统称Term，即一个搜索单元
> 
> - 返回有价值信息  
对得到的文档进行排序

### 建立索引

采用了BSBI算法使用python程序来构建倒排索引，具体过程参照下图：

![](https://github.com/daren996/Information-Retrieval-System-for-Amazon-Products/blob/master/BSBI.png)

这里我假定每一个doc都是有id的，我们称之为doc\_id。除此之外，还定义了一些其他的量，例如word\_id，以及：

	self.word\_set = set()  # all words
	self.word2id\_map = {}   # map : word -> word\_id
	self.index = {}         # map & set : word\_id -> docs\_set
	self.D = 0              # int : The total number of documents
	self.W = 0              # int : The total number of words

由于数据并不太多，目前假定内存是可以处理整个的index的。

在构建索引表的时候，采用了外层diction、内层set的方式，原因是diction基于哈希表，查找速度超过list，而set的合并、删除、判断是否存在等操作效率更高。

将索引表写入文件的时候使用了python的pickle库，将index、word_set、word2id_map，例如：

        with open(conf.index_path, 'wb') as out_file:
            out_file.write(pickle.dumps(self.index))

代码在index.py里。

