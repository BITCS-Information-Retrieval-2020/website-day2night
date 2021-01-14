<template>
  <el-container>
    <el-header>
       <search-bar @searchResults="searchResults"></search-bar>
       {{ results }}
    </el-header>
    <el-main>
      <!-- 左侧内容 -->
      <div id="u103" class="ax_default _二级标题">
        <div id="u103_div" class=""></div>
        <div id="u103_text" class="text ">
          <p><span>来源</span></p>
        </div>
      </div>

      <!-- 左侧内容 -->
      <div id="u104" class="ax_default _二级标题">
        <div id="u104_div" class=""></div>
        <div id="u104_text" class="text ">
          <p><span>年度</span></p>
        </div>
      </div>

      <!-- 左侧内容 -->
      <div id="u105" class="ax_default _三级标题">
        <div id="u105_div" class=""></div>
        <div id="u105_text" class="text ">
          <p><span>CrossMinds</span></p>
        </div>
      </div>

      <!--  左侧内容 -->
      <div id="u106" class="ax_default _三级标题">
        <div id="u106_div" class=""></div>
        <div id="u106_text" class="text ">
          <p><span>ACL Anthology</span></p>
        </div>
      </div>

      <!-- 左侧内容 -->
      <div id="u107" class="ax_default _三级标题">
        <div id="u107_div" class=""></div>
        <div id="u107_text" class="text ">
          <p><span>Papers With Code</span></p>
        </div>
      </div>

      <!-- 左侧内容 -->
      <div id="u108" class="ax_default _三级标题">
        <div id="u108_div" class=""></div>
        <div id="u108_text" class="text ">
          <p><span>PaperWeekly</span></p>
        </div>
      </div>

      <!-- Unnamed (矩形) -->
      <div id="u109" class="ax_default _三级标题">
        <div id="u109_div" class=""></div>
        <div id="u109_text" class="text ">
          <p><span>DBLP</span></p>
        </div>
      </div>

      <!-- 左侧内容 -->
      <div id="u110" class="ax_default _三级标题">
        <div id="u110_div" class=""></div>
        <div id="u110_text" class="text ">
          <p><span>Semantic Scholar</span></p>
        </div>
      </div>

      <!-- 左侧内容 -->
      <div id="u111" class="ax_default _三级标题">
        <div id="u111_div" class=""></div>
        <div id="u111_text" class="text ">
          <p><span>IEEE Xplore</span></p>
        </div>
      </div>

      <!-- 左侧内容 -->
      <div id="u112" class="ax_default _三级标题">
        <div id="u112_div" class=""></div>
        <div id="u112_text" class="text ">
          <p><span>2020</span></p>
        </div>
      </div>
      <!-- 左侧内容 -->
      <div id="u122" class="ax_default _三级标题">
        <div id="u122_div" class=""></div>
        <div id="u122_text" class="text ">
          <p><span>2019</span></p>
        </div>
      </div>

      <!-- 左侧内容 -->
      <div id="u123" class="ax_default _三级标题">
        <div id="u123_div" class=""></div>
        <div id="u123_text" class="text ">
          <p><span>2018</span></p>
        </div>
      </div>

      <!-- 左侧内容 -->
      <div id="u124" class="ax_default _三级标题">
        <div id="u124_div" class=""></div>
        <div id="u124_text" class="text ">
          <p><span>2017</span></p>
        </div>
      </div>
      <!-- 列表上方 -->
      <div id="u125" class="ax_default _三级标题">
        <div id="u125_div" class=""></div>
        <div id="u125_text" class="text ">
          <p><span>最新</span></p>
        </div>
      </div>

      <!-- 列表上方 -->
      <div id="u126" class="ax_default _三级标题">
        <div id="u126_div" class=""></div>
        <div id="u126_text" class="text ">
          <p><span>最相关</span></p>
        </div>
      </div>


      <!-- 第一个文章框 -->
      <div id="u97" class="ax_default box_2" >
          <div id="u97_div" class=""></div>
        </div>
        <!-- 第一个文章题目 -->
        <div id="u99" class="ax_default _三级标题">
          <div id="u99_text" class="text ">
            <p><span>Autonomous AI Tractor | Monarch</span></p>
          </div>
        </div>
        <!-- 第一个文章的作者、出版机构、时间 -->
        <div id="u100" class="ax_default _文本段落">
          <div id="u100_text" class="text ">
            <p>
              <span style="font-family:'PingFangSC-Regular', 'PingFang SC', sans-serif;">
                作者：Han Zhang </span>
              </p>
            <p>
              <span style="font-family:'PingFangSC-Regular', 'PingFang SC', sans-serif;">
                出版组织：/International conference on machine learning. PMLR
              </span>
            </p>
            <p>
              <span style="font-family:'PingFangSC-Regular', 'PingFang SC', sans-serif;">时间：2019</span>
            </p>
          </div>
        </div>
        <!-- 第一个文章的pdf按钮 -->
        <div id="u101" class="ax_default _图片_">
          <el-button type="primary" round>PDF</el-button></div>
        <!-- 第一个文章的code按钮 -->
       <div id="u102" class="ax_default _图片_">
         <el-button type="primary" round>Code</el-button>
          </div>

         <!-- 第二个文章框 -->
      <div id="u97_2" class="ax_default box_2" >
          <div id="u97_2_div" class=""></div>
          <div id="u97_2_ext" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>
        <!-- 第二个文章题目 -->
        <div id="u99_2" class="ax_default _三级标题">
          <div id="u99_2_div" class=""></div>
          <div id="u99_2_text" class="text ">
            <p><span>Autonomous AI Tractor | Monarch</span></p>
          </div>
        </div>
        <!-- 第二个文章的作者、出版机构、时间 -->
        <div id="u100_2" class="ax_default _文本段落">
          <div id="u100_2_div" class=""></div>
          <div id="u100_2_text" class="text ">
            <p>
              <span style="font-family:'PingFangSC-Regular', 'PingFang SC', sans-serif;">
                作者：Han Zhang </span>
               </p>
            <p>
              <span style="font-family:'PingFangSC-Regular', 'PingFang SC', sans-serif;">
                出版组织：/International conference on machine learning. PMLR
              </span>
            </p>
            <p>
              <span style="font-family:'PingFangSC-Regular', 'PingFang SC', sans-serif;">时间：2019</span>
            </p>
          </div>
        </div>
        <!-- 第二个文章的pdf按钮 -->
        <div id="u101_2" class="ax_default _图片_">
          <el-button type="primary" round>PDF</el-button></div>
        <!-- 第二个文章的code按钮 -->
       <div id="u102_2" class="ax_default _图片_">
         <el-button type="primary" round>Code</el-button>
          </div> 



         <!-- 第三个文章框 -->
      <div id="u97_3" class="ax_default box_2" >
          <div id="u97_3_div" class=""></div>
          <div id="u97_3_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>
        <!-- 第三个文章题目 -->
        <div id="u99_3" class="ax_default _三级标题">
          <div id="u99_3_div" class=""></div>
          <div id="u99_3_text" class="text ">
            <p><span>Autonomous AI Tractor | Monarch</span></p>
          </div>
        </div>
        <!-- 第三个文章的作者、出版机构、时间 -->
        <div id="u100_3" class="ax_default _文本段落">
          <div id="u100_3_div" class=""></div>
          <div id="u100_3_text" class="text ">
            <p>
              <span style="font-family:'PingFangSC-Regular', 'PingFang SC', sans-serif;">
                作者：Han Zhang </span>
               </p>
            <p>
              <span style="font-family:'PingFangSC-Regular', 'PingFang SC', sans-serif;">
                出版组织：/International conference on machine learning. PMLR
              </span>
            </p>
            <p>
              <span style="font-family:'PingFangSC-Regular', 'PingFang SC', sans-serif;">时间：2019</span>
            </p>
          </div>
        </div>
        <!-- 第三个文章的pdf按钮 -->
        <div id="u101_3" class="ax_default _图片_">
          <el-button type="primary" round>PDF</el-button></div>
        <!-- 第三个文章的code按钮 -->
       <div id="u102_3" class="ax_default _图片_">
         <el-button type="primary" round>Code</el-button>
          </div> 

         <!-- 第四个文章框 -->
      <div id="u97_4" class="ax_default box_2" >
          <div id="u97_4_div" class=""></div>
          <div id="u97_4_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>
        <!-- 第四个文章题目 -->
        <div id="u99_4" class="ax_default _三级标题">
          <div id="u99_4_div" class=""></div>
          <div id="u99_4_text" class="text ">
            <p><span>Autonomous AI Tractor | Monarch</span></p>
          </div>
        </div>
        <!-- 第四个文章的作者、出版机构、时间 -->
        <div id="u100_4" class="ax_default _文本段落">
          <div id="u100_4_div" class=""></div>
          <div id="u100_4_text" class="text ">
            <p>
              <span style="font-family:'PingFangSC-Regular', 'PingFang SC', sans-serif;">
                作者：Han Zhang(Rutgers university) 、Ian Goodfellow（Google Brain）</span>
              </p>
            <p>
              <span style="font-family:'PingFangSC-Regular', 'PingFang SC', sans-serif;">
                出版组织：/International conference on machine learning. PMLR
              </span>
            </p>
            <p>
              <span style="font-family:'PingFangSC-Regular', 'PingFang SC', sans-serif;">时间：2019</span>
            </p>
          </div>
        </div>
        <!-- 第四个文章的pdf按钮 -->
        <div id="u101_4" class="ax_default _图片_">
          <el-button type="primary" round>PDF</el-button></div>
        <!-- 第四个文章的code按钮 -->
       <div id="u102_4" class="ax_default _图片_">
         <el-button type="primary" round>Code</el-button>
          </div> 

        <!-- 翻页按钮-->
         <el-pagination background layout="prev, pager, next" :total="1000">
         </el-pagination>
    </el-main>
    <el-footer>
      <!-- 页面底部 -->
      <div id="u187" class="ax_default _二级标题">
        <div id="u187_div" class=""></div>
        <div id="u187_text" class="text ">
          <p><span>关于我们</span></p>
        </div>
      </div>

      <!-- Unnamed (矩形) -->
      <div id="u188" class="ax_default _二级标题">
        <div id="u188_div" class=""></div>
        <div id="u188_text" class="text ">
          <p><span>联系我们</span></p>
        </div>
      </div>

      <!-- Unnamed (矩形) -->
      <div id="u189" class="ax_default _文本段落">
        <div id="u189_div" class=""></div>
        <div id="u189_text" class="text ">
          <p><span style="font-family:'Arial Normal', 'Arial', sans-serif;font-weight:400;">©2020&nbsp; </span><span style="font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;font-weight:700;">Paper&nbsp; Day2night</span></p>
        </div>
      </div>
      
    </el-footer>
  </el-container>
</template>

<script>
import SearchBar from "common/SearchBar.vue"
export default {
  components: { SearchBar },
  name: "Result",
  data() {
    return {
      //results: [],
      results:[
        {title:"Autonomous AI Tractor | Monarch",
        authors:"Han Zhang(Rutgers university) 、Ian Goodfellow（Google Brain）",
        time:"2019",
        pdfurl:"http://d.wanfangdata.com.cn/periodical/bjyddx201003001",
        codeurl:"https://github.com/BITCS-Information-Retrieval-2020/website-day2night/blob/backend/data/README.md",
        },
        {title:"Autonomous AI Tractor | Monarch",
        authors:"Han Zhang(Rutgers university) 、Ian Goodfellow（Google Brain）",
        time:"2019",
        pdfurl:"http://d.wanfangdata.com.cn/periodical/bjyddx201003001",
        codeurl:"https://github.com/BITCS-Information-Retrieval-2020/website-day2night/blob/backend/data/README.md",
        },
        {title:"Autonomous AI Tractor | Monarch",
        authors:"Han Zhang(Rutgers university) 、Ian Goodfellow（Google Brain）",
        time:"2019",
        pdfurl:"http://d.wanfangdata.com.cn/periodical/bjyddx201003001",
        codeurl:"https://github.com/BITCS-Information-Retrieval-2020/website-day2night/blob/backend/data/README.md",
        },
        {title:"Autonomous AI Tractor | Monarch",
        authors:"Han Zhang(Rutgers university) 、Ian Goodfellow（Google Brain）",
        time:"2019",
        pdfurl:"http://d.wanfangdata.com.cn/periodical/bjyddx201003001",
        codeurl:"https://github.com/BITCS-Information-Retrieval-2020/website-day2night/blob/backend/data/README.md",
        },
        {title:"Autonomous AI Tractor | Monarch",
        authors:"Han Zhang(Rutgers university) 、Ian Goodfellow（Google Brain）",
        time:"2019",
        pdfurl:"http://d.wanfangdata.com.cn/periodical/bjyddx201003001",
        codeurl:"https://github.com/BITCS-Information-Retrieval-2020/website-day2night/blob/backend/data/README.md",
        },
        {title:"Autonomous AI Tractor | Monarch",
        authors:"Han Zhang(Rutgers university) 、Ian Goodfellow（Google Brain）",
        time:"2019",
        pdfurl:"http://d.wanfangdata.com.cn/periodical/bjyddx201003001",
        codeurl:"https://github.com/BITCS-Information-Retrieval-2020/website-day2night/blob/backend/data/README.md",
        },
        {title:"Autonomous AI Tractor | Monarch",
        authors:"Han Zhang(Rutgers university) 、Ian Goodfellow（Google Brain）",
        time:"2019",
        pdfurl:"http://d.wanfangdata.com.cn/periodical/bjyddx201003001",
        codeurl:"https://github.com/BITCS-Information-Retrieval-2020/website-day2night/blob/backend/data/README.md",
        },
        {title:"Autonomous AI Tractor | Monarch",
        authors:"Han Zhang(Rutgers university) 、Ian Goodfellow（Google Brain）",
        time:"2019",
        pdfurl:"http://d.wanfangdata.com.cn/periodical/bjyddx201003001",
        codeurl:"https://github.com/BITCS-Information-Retrieval-2020/website-day2night/blob/backend/data/README.md",
        },
        ],
    }
  },
  methods: {
    // 获取搜索结果
    searchResults(results) {
      console.log(results)
      this.results = results
    },
  },
  mounted() {
    //获取搜索结果
    this.results = this.$route.params.results
  },
}
</script>

<style>
.el-header {
  background-color: #fdfdfdf2;
  height: 130px;
  position: absolute;
  width: 1352px;
  padding: 0px;
  }
  
.el-main {
    position: absolute;
    top: 140px;
    width: 1352px;
    height: 1130px;
    background-color:rgba(242, 242, 242, 1);
    border: none;
    border-radius: 0px;
    -moz-box-shadow: none;
    -webkit-box-shadow: none;
    box-shadow: none;
}
.el-footer{
    position: absolute;
    top: 1270px;
    width: 1352px;
    height: 1130px;
    background-color: rgba(38, 41, 49, 1);
    border: none;
    border-radius: 0px;
    -moz-box-shadow: none;
    -webkit-box-shadow: none;
    box-shadow: none;
}
.el-pagination{
  position: absolute;
  left:350px;
  top:1050px;
  width:900px;
    background-color:rgba(242, 242, 242, 1);
}
#u187_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top: 0px;
  width:72px;
  height:21px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
  font-size:18px;
  color:#FFFFFF;
}
#u187 {
  border-width:0px;
  position:absolute;
  left:169px;
  top: 0px;
  width:72px;
  height:21px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
  font-size:18px;
  color:#FFFFFF;
}
#u187 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u187_text {
  border-width:0px;
  white-space:nowrap;
  text-transform:none;
}
#u188_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:72px;
  height:21px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
  font-size:18px;
  color:#FFFFFF;
}
#u188 {
  border-width:0px;
  position:absolute;
  left:381px;
  top:0px;
  width:72px;
  height:21px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
  font-size:18px;
  color:#FFFFFF;
}
#u188 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u188_text {
  border-width:0px;
  white-space:nowrap;
  text-transform:none;
}
#u189_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:300px;
  height:16px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-size:14px;
  color:#FFFFFF;
}
#u189 {
  border-width:0px;
  position:absolute;
  left:574px;
  top:0px;
  width:300px;
  height:16px;
  display:flex;
  font-size:14px;
  color:#FFFFFF;
}
#u189 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u189_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
}
#u103_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:247px;
  height:28px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
  color:#7F7F7F;
}
#u103 {
  border-width:0px;
  position:absolute;
  left:-55px;
  top:10px;
  width:247px;
  height:28px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
  color:#7F7F7F;
}
#u103 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u103_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
}
#u104_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:247px;
  height:28px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
  color:#7F7F7F;
}
#u104 {
  border-width:0px;
  position:absolute;
  left:-55px;
  top:340px;
  width:247px;
  height:28px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
  color:#7F7F7F;
}
#u104 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u104_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
}
#u105_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:104px;
  height:21px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
}
#u105 {
  border-width:0px;
  position:absolute;
  left:45px;
  top:50px;
  width:104px;
  height:21px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
}
#u105 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u105_text {
  border-width:0px;
  white-space:nowrap;
  text-align:left;
  text-transform:none;
}
#u106_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:130px;
  height:21px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
}
#u106 {
  border-width:0px;
  position:absolute;
  left:45px;
  top:80px;
  width:130px;
  height:21px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
}
#u106 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u106_text {
  border-width:0px;
    text-align:left;

  white-space:nowrap;
  text-transform:none;
}
#u107_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:154px;
  height:21px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
}
#u107 {
  border-width:0px;
  position:absolute;
  left:45px;
  top:120px;
  width:154px;
  height:21px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
}
#u107 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u107_text {
  border-width:0px;
  white-space:nowrap;
    text-align:left;

  text-transform:none;
}
#u108_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:112px;
  height:21px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
}
#u108 {
  border-width:0px;
  position:absolute;
  left:45px;
  top:160px;
  width:112px;
  height:21px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
}
#u108 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u108_text {
  border-width:0px;
  white-space:nowrap;
    text-align:left;

  text-transform:none;
}
#u109_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:49px;
  height:21px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
}
#u109 {
  border-width:0px;
  position:absolute;
  left:45px;
  top:200px;
  width:49px;
  height:21px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
}
#u109 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u109_text {
  border-width:0px;
  white-space:nowrap;
    text-align:left;

  text-transform:none;
}
#u110_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:152px;
  height:21px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
}
#u110 {
  border-width:0px;
  position:absolute;
  left:45px;
  top:240px;
  width:152px;
  height:21px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
}
#u110 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u110_text {
  border-width:0px;
  white-space:nowrap;
    text-align:left;

  text-transform:none;
}
#u111_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:103px;
  height:21px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
}
#u111 {
  border-width:0px;
  position:absolute;
  left:45px;
  top:280px;
  width:103px;
  height:21px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
}
#u111 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u111_text {
  border-width:0px;
  white-space:nowrap;
    text-align:left;

  text-transform:none;
}
#u112_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:41px;
  height:21px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
}
#u112 {
  border-width:0px;
  position:absolute;
  left:50px;
  top:380px;
  width:41px;
  height:21px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
}
#u112 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u112_text {
  border-width:0px;
  white-space:nowrap;
    text-align:left;

  text-transform:none;
}
#u122_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:41px;
  height:21px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
}
#u122 {
  border-width:0px;
  position:absolute;
  left:50px;
  top:420px;
  width:41px;
  height:21px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
}
#u122 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u122_text {
  border-width:0px;
  white-space:nowrap;
    text-align:left;

  text-transform:none;
}
#u123_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:41px;
  height:21px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
}
#u123 {
  border-width:0px;
  position:absolute;
  left:50px;
  top:460px;
  width:41px;
  height:21px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
}
#u123 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u123_text {
  border-width:0px;
    text-align:left;

  white-space:nowrap;
  text-transform:none;
}
#u124_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:41px;
  height:21px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
}
#u124 {
  border-width:0px;
  position:absolute;
  left:50px;
  top:500px;
  width:41px;
  height:21px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
}
#u124 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u124_text {
  border-width:0px;
    text-align:left;

  white-space:nowrap;
  text-transform:none;
}
#u125_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:40px;
  height:21px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
  font-size:20px;
  color:#4A84E8;
}
#u125 {
  border-width:0px;
  position:absolute;
  left:333px;
  top:0px;
  width:40px;
  height:21px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
  font-size:20px;
  color:#4A84E8;
}
#u125 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u125_text {
  border-width:0px;
  white-space:nowrap;
  text-transform:none;
}
#u126_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:60px;
  height:21px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
  font-size:20px;
}
#u126 {
  border-width:0px;
  position:absolute;
  left:426px;
  top:0px;
  width:60px;
  height:21px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
  font-size:20px;
}
#u126 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u126_text {
  border-width:0px;
  white-space:nowrap;
  text-transform:none;
}

#u97_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:979px;
  height:206px;
  background:inherit;
  background-color:rgba(255, 255, 255, 1);
  border:none;
  border-radius:0px;
  -moz-box-shadow:5px 5px 9px rgba(0, 0, 0, 0.349019607843137);
  -webkit-box-shadow:5px 5px 9px rgba(0, 0, 0, 0.349019607843137);
  box-shadow:5px 5px 9px rgba(0, 0, 0, 0.349019607843137);
}
#u97 {
  border-width:0px;
  position:absolute;
  left:317px;
  top:100px;
  width:979px;
  height:206px;
  display:flex;
}
#u99 {
  border-width:0px;
  position:absolute;
  left:350px;
  top:110px;
  width:547px;
  height:22px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
  font-size:22px;
}
#u99_text {
  border-width:0px;
  text-align:left;
  word-wrap:break-word;
  text-transform:none;
}
#u100_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:703px;
  height:144px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-size:18px;
}
#u100 {
  border-width:0px;
  position:absolute;
  left:350px;
  top:155px;
  width:703px;
  height:144px;
  display:flex;
  font-size:18px;
}
#u100_text {
  border-width:0px;
  text-align:left;
  word-wrap:break-word;
  text-transform:none;
}
#u101 {
  border-width:0px;
  position:absolute;
  left:1050px;
  top:160px;
  width:130px;
  height:37px;
  display:flex;
}
#u102 {
  border-width:0px;
  position:absolute;
  left:1050px;
  top:220px;
  width:129px;
  height:37px;
  display:flex;
}


#u97_2_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:979px;
  height:206px;
  background:inherit;
  background-color:rgba(255, 255, 255, 1);
  border:none;
  border-radius:0px;
  -moz-box-shadow:5px 5px 9px rgba(0, 0, 0, 0.349019607843137);
  -webkit-box-shadow:5px 5px 9px rgba(0, 0, 0, 0.349019607843137);
  box-shadow:5px 5px 9px rgba(0, 0, 0, 0.349019607843137);
}
#u97_2 {
  border-width:0px;
  position:absolute;
  left:317px;
  top:330px;
  width:979px;
  height:206px;
  display:flex;
}
#u99_2 {
  border-width:0px;
  position:absolute;
  left:350px;
  top:340px;
  width:547px;
  height:22px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
  font-size:22px;
}
#u99_2_text {
  border-width:0px;
  text-align:left;
  word-wrap:break-word;
  text-transform:none;
}
#u100_2_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:703px;
  height:144px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-size:18px;
}
#u100_2 {
  border-width:0px;
  position:absolute;
  left:350px;
  top:385px;
  width:703px;
  height:144px;
  display:flex;
  font-size:18px;
}
#u100_2_text {
  border-width:0px;
  text-align:left;
  word-wrap:break-word;
  text-transform:none;
}
#u101_2 {
  border-width:0px;
  position:absolute;
  left:1050px;
  top:390px;
  width:130px;
  height:37px;
  display:flex;
}
#u102_2 {
  border-width:0px;
  position:absolute;
  left:1050px;
  top:450px;
  width:129px;
  height:37px;
  display:flex;
}

#u97_3_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:979px;
  height:206px;
  background:inherit;
  background-color:rgba(255, 255, 255, 1);
  border:none;
  border-radius:0px;
  -moz-box-shadow:5px 5px 9px rgba(0, 0, 0, 0.349019607843137);
  -webkit-box-shadow:5px 5px 9px rgba(0, 0, 0, 0.349019607843137);
  box-shadow:5px 5px 9px rgba(0, 0, 0, 0.349019607843137);
}
#u97_3 {
  border-width:0px;
  position:absolute;
  left:317px;
  top:560px;
  width:979px;
  height:206px;
  display:flex;
}
#u99_3 {
  border-width:0px;
  position:absolute;
  left:350px;
  top:570px;
  width:547px;
  height:22px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
  font-size:22px;
}
#u99_3_text {
  border-width:0px;
  text-align:left;
  word-wrap:break-word;
  text-transform:none;
}
#u100_3_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:703px;
  height:144px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-size:18px;
}
#u100_3 {
  border-width:0px;
  position:absolute;
  left:350px;
  top:615px;
  width:703px;
  height:144px;
  display:flex;
  font-size:18px;
}
#u100_3_text {
  border-width:0px;
  text-align:left;
  word-wrap:break-word;
  text-transform:none;
}
#u101_3 {
  border-width:0px;
  position:absolute;
  left:1050px;
  top:620px;
  width:130px;
  height:37px;
  display:flex;
}
#u102_3 {
  border-width:0px;
  position:absolute;
  left:1050px;
  top:680px;
  width:129px;
  height:37px;
  display:flex;
}


#u97_4_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:979px;
  height:206px;
  background:inherit;
  background-color:rgba(255, 255, 255, 1);
  border:none;
  border-radius:0px;
  -moz-box-shadow:5px 5px 9px rgba(0, 0, 0, 0.349019607843137);
  -webkit-box-shadow:5px 5px 9px rgba(0, 0, 0, 0.349019607843137);
  box-shadow:5px 5px 9px rgba(0, 0, 0, 0.349019607843137);
}
#u97_4 {
  border-width:0px;
  position:absolute;
  left:317px;
  top:790px;
  width:979px;
  height:206px;
  display:flex;
}
#u99_4 {
  border-width:0px;
  position:absolute;
  left:350px;
  top:800px;
  width:547px;
  height:22px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial', sans-serif;
  font-weight:700;
  font-style:normal;
  font-size:22px;
}
#u99_4_text {
  border-width:0px;
  text-align:left;
  word-wrap:break-word;
  text-transform:none;
}
#u100_4_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:703px;
  height:144px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-size:18px;
}
#u100_4 {
  border-width:0px;
  position:absolute;
  left:350px;
  top:845px;
  width:703px;
  height:144px;
  display:flex;
  font-size:18px;
}
#u100_4_text {
  border-width:0px;
  text-align:left;
  word-wrap:break-word;
  text-transform:none;
}
#u101_4 {
  border-width:0px;
  position:absolute;
  left:1050px;
  top:850px;
  width:130px;
  height:37px;
  display:flex;
}
#u102_4 {
  border-width:0px;
  position:absolute;
  left:1050px;
  top:910px;
  width:129px;
  height:37px;
  display:flex;
}
</style>