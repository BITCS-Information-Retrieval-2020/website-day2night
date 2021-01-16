<template>
  <el-row id="introbar">
    <el-col id="info" :span="20">
      <el-row>
        <h2 id="title">{{title}}</h2>
        <p id="year">出版时间：{{year}}年</p>
      </el-row>
      <el-row >
        <p>
          作者： {{author}}
        </p>

      </el-row>
      <el-row style="margin-bottom: 50px">
        <p style="margin-bottom: 0px">摘要：</p>
        <p id="abs">{{abstract}}</p>
      </el-row>
      <el-row id="url" style="font-size: 15px;" >
        <p :class="{urlform:true}">论文地址:
          <a id="paperurl"
             :href="paperurl"
             style="margin-left: 10px"
             target="_blank">
            {{paperurl}}
          </a>
        </p>
        <p :class="{urlform:true}">代码地址:
          <a id="codeurl"
             :href="codeurl"
             style="margin-left: 10px"
             target="_blank" >
            {{codeurl}}
          </a>
        </p>
        <p :class="{urlform:true}">视频地址:
          <a id="videourl"
             :href="videourl"
             style="margin-left: 10px"
             target="_blank" >
            {{videourl}}
          </a>
        </p>
<!--        {{detail}}-->
      </el-row>
    </el-col>
    <el-col  :span="4">
      <p style="font-size: 15px;">论文来源</p>
      <div id="source" >{{source}}</div>
    </el-col>

  </el-row>
</template>

<script>
export default {
  name: "introducton",
  props:["detail"],
  data() {
    return {
      abstract:"Effective palliation of malignant biliary obstruction with conventional 10 or 12 French gauge straight polyethylene endoprostheses is limited by stent occlusion, which typically occurs four to five months after insertion. Short term follow up studies of self expanding metal stents (Wallstent, Schneider, UK) in the treatment of patients with malignant biliary obstruction have shown that their use is associated with fewer episodes of stent occlusion compared with plastic stents. There are few data, however, on the longterm patency and durability of metal stents in malignant disease. Between May 1989 and May 1992, metal stents were inserted in 28 patients with malignant bile duct strictures secondary to ampullary tumour (n = 10), pancreatic carcinoma (n = 10), cholangiocarcinoma (n = 7), and porta hepatis nodes from colorectal carcinoma (n = 1). The follow up of these patients until May 1993 is reported with a median follow up of 14.6 months. Twenty two of 28 (78.6%) patients remained free of jaundice or cholangitis. The median period of stent patency was 8.2 months (range 1.0-32.5). Thirteen patients represented with jaundice or cholangitis and endoscopic retrograde",
    }
  },
  computed: {
    title(){
      return this.detail.title
    },
    year() {
      return this.detail.year
    },
    author() {
      return this.detail.authors
    },
    paperurl() {
      if (this.detail.publicationUrl=="") {
        return "无"
      }
      return this.detail.publicationUrl
    },
    codeurl() {
      if (this.detail.codeUrl=="") {
        return "无"
      }
      return this.detail.codeUrl
    },
    videourl() {
      if (this.detail.videoUrl=="") {
        return "无"
      }
      return this.detail.videoUrl
    },
    source() {
      return this.detail.publicationOrg
    },
  },
  methods: {
    changeColor() {
      this.paperurlact=true;
    }
  },
}
</script>

<style scoped>
#introbar{
  margin-top: 20px;
  width: 90%;
  margin-left: 5%;
  margin-bottom: 20px;
}
#info{
  background: white;
  padding-left: 20px;
  text-align:left;
  box-shadow:3px 3px 5px 0px #787878;
}
#title{
  color: #4a83e7;
  margin-bottom: 5px;
}
#year{
  margin-top: 5px;
}
#abs{
  padding-left: 40px;
  padding-right: 40px;
}
#source{
  color: #f0f0f0;
  font-size: 25px;
  font-weight: bolder;
  background: #4a84e8f2;
  margin-left: 15%;
  height: 50px;
  width: 70%;
  text-align:center;
  line-height: 50px;
  box-shadow:3px 3px 5px 0px #787878;
}
.urlform{
  padding-right: 10px;
  margin-top: 15px;
  margin-bottom: 15px;
}
.activeColor {
  color: red;
}
</style>