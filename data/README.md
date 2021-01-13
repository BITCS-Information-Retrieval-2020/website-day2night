
# 接口文档
### 1. 检索结果页
描述：从前端接收的数据形式，即前端的请求格式
#### URL   
 /results
#### HTTP请求方式
**GET**  /results?type=0&query=game&page=1

#### HTTP返回格式
JSON

#### HTTP请求参数说明
| 参数       | 类型     | 必需     | 描述       |
| ------------- |:----------:| ---------:|:-------------:| 
| type       | string      | 是      | 检索类型 0表示全部字段检索，1表示高级检索，2表示视频定位|
| query   | string    | 是(二选一) | type0、type2 的检索字段|
| query   | dict     | 是(二选一) | type1的检索字段|
| page       | string      | 是      |分页后当前页面序号|


##### 示例

    // type 0 表示全部字段检索，在基本搜索框和高级检索的“全部”选项中使用
    {
        "type": 0,
        "query": "GNN"
    }
    // type 1 表示高级检索，不需要的字段设为空字符串，operator表示从
    //第二个字段开始每个字段的运算符，空字段对应的操作符也为空字符串
    {
        "type": 1,
        "query":{
            "title": "GNN",
            "author": "Hinton",
            "abstract": "",
            "content": "this paper proposed ...",
	    "operator": ["OR", "AND", "", "NOT"]
        }
        
    }
    // type 2 表示视频定位
    {
        "type": 2,
        "query": "GNN"
    }

#### 返回结果说明
返回 [{},{},{},……]

| 参数       | 类型     | 描述     |
| ------------- |:----------:| ---------:|
| id         | string    |文章唯一id |
| title       | string    |文章标题|
| authos       | string    |摘要|
|publicationOrg |string |发表刊物|
|year        |int       |发表时间 |
|pdfUrl     |string    |pdf链接|
|pdfPath   |string |      绝对路径(下载地址)|
|publicationUrl  |string   |发表刊物地址|
|codeUrl   |string           |代码地址 |
|datasetUrl  |string     | 数据集地址|
|videoUrl |string               |视频地址|
|videoPath |string  |      视频下载地址|
|pdfText |string   |         文章内容|
|videoStruct |list   |视频内容(开始时间、结束时间、句子内容)|

##### 示例


     [   {
            "_id": 1, //按照相关度进行排序 数字越小越相关
            "title": "[Oral at NeurIPS 2020] DVERGE: Diversifying Vulnerabilities for Enhanced Robust Generation of Ensembles",
            "authors": "Huanrui Yang, Jingyang Zhang, Hongliang Dong, Nathan Inkawhich, Andrew Gardner, Andrew Touchet, Wesley Wilkes, Heath Berry, Hai Li",
            "abstract": "Recent research finds CNN models...",
            "publicationOrg": "NeurIPS",
            "year": 2020,
            "pdfUrl": "...",
            "pdfPath": ".../searcher/data/PDFs/xx.pdf",// 绝对路径
            "publicationUrl": "https://papers.nips.cc/paper/2020/hash/3ad7c2ebb96fcba7cda0cf54a2e802f5-Abstract.html",
            "codeUrl": "https://github.com/zjysteven/DVERGE",
            "datasetUrl": "https://drive.google.com/drive/folders/1i96Bk_bCWXhb7afSNp1t3woNjO1kAMDH?usp=sharing",
            "videoUrl": "",
            "videoPath": ".../searcher/data/videos/xx.*",// 绝对路径
            "pdfText": "Alternatively, ensemble methods are proposed to induce sub-models...",
            "videoStruct": [
                {
                    "timeStart": "hh-mm-ss",
                    "timeEnd": "hh-mm-ss",
                    "sentence": "Only small clean accuracy drop is observed in the process."
                }
            ]
        },
       {
            "_id": 1, //按照相关度进行排序 数字越小越相关
            "title": "[Oral at NeurIPS 2020] DVERGE: Diversifying Vulnerabilities for Enhanced Robust Generation of Ensembles",
            "authors": "Huanrui Yang, Jingyang Zhang, Hongliang Dong, Nathan Inkawhich, Andrew Gardner, Andrew Touchet, Wesley Wilkes, Heath Berry, Hai Li",
            "abstract": "Recent research finds CNN models...",
            "publicationOrg": "NeurIPS",
            "year": 2020,
            "pdfUrl": "...",
            "pdfPath": ".../searcher/data/PDFs/xx.pdf",// 绝对路径
            "publicationUrl": "https://papers.nips.cc/paper/2020/hash/3ad7c2ebb96fcba7cda0cf54a2e802f5-Abstract.html",
            "codeUrl": "https://github.com/zjysteven/DVERGE",
            "datasetUrl": "https://drive.google.com/drive/folders/1i96Bk_bCWXhb7afSNp1t3woNjO1kAMDH?usp=sharing",
            "videoUrl": "",
            "videoPath": ".../searcher/data/videos/xx.*",// 绝对路径
            "pdfText": "Alternatively, ensemble methods are proposed to induce sub-models...",
            "videoStruct": [
                {
                    "timeStart": "hh-mm-ss",
                    "timeEnd": "hh-mm-ss",
                    "sentence": "Only small clean accuracy drop is observed in the process."
                }
            ]
        }
    ]



```python

```


### 2. 热门文章请求
描述：返回热门搜索文章 置于主页
#### URL   
 /hot
#### HTTP请求方式
**GET**  

#### HTTP返回格式
JSON

#### HTTP请求参数说明
|参数|类型|必需|描述|
|---|---|---|---|
|number|int|否|返回的热门文章数目（否则为默认值）|


#### 返回结果说明
|参数|类型|描述|
|---|---|---|
|_id|string|文章唯一id|
|title|string|文章标题|
##### 示例
```

{
    [
         {
          '_id':"5",
          '_title':'基于深度学习的。。'
         },
         {
         '_id':"5",
         '_title':'基于深度学习的。。'
        }
     ]
} 
```
 
### 3. 文章详情
描述：返回文章具体信息
#### URL   
/detail
#### HTTP请求方式
**GET** 

#### HTTP返回格式
JSON

#### HTTP请求参数说明
|参数|类型|必需|描述|
|---|---|---|---|
|_id|string|是|文章唯一id|


#### 返回结果说明

| 参数       | 类型     | 描述     |
| ------------- |:----------:| ---------:|
| id         | string    |文章唯一id |
| title       | string    |文章标题|
| authos       | string    |摘要|
|publicationOrg |string |发表刊物|
|year        |int       |发表时间 |
|pdfUrl     |string    |pdf链接|
|pdfPath   |string |      绝对路径(下载地址)|
|publicationUrl  |string   |发表刊物地址|
|codeUrl   |string           |代码地址 |
|datasetUrl  |string     | 数据集地址|
|videoUrl |string               |视频地址|
|videoPath |string  |      视频下载地址|
|pdfText |string   |         文章内容|
|videoStruct |list   |视频内容(开始时间、结束时间、句子内容)|
##### 示例
```

    {
        "_id": 1, 
        "title": "[Oral at NeurIPS 2020] DVERGE: Diversifying Vulnerabilities for Enhanced Robust Generation of Ensembles",
        "authors": "Huanrui Yang, Jingyang Zhang, Hongliang Dong, Nathan Inkawhich, Andrew Gardner, Andrew Touchet, Wesley Wilkes, Heath Berry, Hai Li",
        "abstract": "Recent research finds CNN models...",
        "publicationOrg": "NeurIPS",
        "year": 2020,
        "pdfUrl": "...",
        "pdfPath": ".../searcher/data/PDFs/xx.pdf",// 绝对路径
        "publicationUrl": "https://papers.nips.cc/paper/2020/hash/3ad7c2ebb96fcba7cda0cf54a2e802f5-Abstract.html",
        "codeUrl": "https://github.com/zjysteven/DVERGE",
        "datasetUrl": "https://drive.google.com/drive/folders/1i96Bk_bCWXhb7afSNp1t3woNjO1kAMDH?usp=sharing",
        "videoUrl": "",
        "videoPath": ".../searcher/data/videos/xx.*",// 绝对路径
        "pdfText": "Alternatively, ensemble methods are proposed to induce sub-models...",
        "videoStruct": [
            {
                "timeStart": "hh-mm-ss",
                "timeEnd": "hh-mm-ss",
                "sentence": "Only small clean accuracy drop is observed in the process."
            }
        ]
    }
```
 ### 4. 下载
描述：在论文详情页，用户可以下载论文
#### URL   
GET  /download/pdf
#### HTTP请求方式
**GET**  

#### HTTP返回格式
JSON

#### HTTP请求参数说明
|参数|类型|必需|描述|
|---|---|---|---|
|_id| string|是| 文章唯一id|


#### 返回结果说明
|参数|类型|描述|
|---|---|---|
|pdfPath|string|绝对路径（下载地址）|
##### 示例
```

//请求：
{
  "_id": "1"
}
//返回：
{
   "pdfPath": ".../searcher/data/PDFs/xx.pdf" // 绝对路径
} 


```

### 5. 自动补全服务
描述：自动补全服务是指用户在搜索框中输入部分文字时，能自动提示对应的文本，例如当用户输入“smart”时，提示以“smart”开头的热门查询词，方便用户操作

#### URL   
GET   /suggest/home
#### HTTP请求方式
**GET**  

#### HTTP返回格式
JSON

#### HTTP请求参数说明
|参数|类型|必需|描述|
|---|---|---|---|
|query|string|是|用户输入的待自动补全的搜索关键词，例如“变”字，utf-8编码，不可为空|


#### 返回结果说明
|参数|类型|描述|
|---|---|---|
|status|string|执行结果，OK为成功，FALL为失败|
|resultcount| int|自动补全结果条数， 如搜索失败，则resultcount值为-1|
|resultdata|string|补全结果，为一个LIST，每一项为一个suggest的字符串|

##### 示例
```
//请求：
{
  "query":"smart",
}
//返回：
{
    "status":"OK",
    "resultcount":10,
    "suggestdata":[
	"smart car",
	"smartguys",
	"samrt and clever"
                  
]} 
```
