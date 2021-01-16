<template>
  <div class="resultItemBox">
    <!-- {{ paper }} -->
    <!-- 第一个文章题目 -->
    <a href="#" @click="toDetail" style="text-decoration: none">
      <el-row class="titleRow">
        <p class="titile_text">
          <span class="titleSpan">{{ title }}</span>
        </p>
      </el-row>
      <!-- 第一个文章的作者、出版机构、时间 -->
      <el-row class="profileRow">
        <p class="text1">
          <span class="zhaiyao"> 摘要：{{ abstract }} </span>
        </p>
        <p class="text">
          <span class="textSpan"> 作者：{{ authors }} </span>
        </p>
        <p class="text">
          <span class="textSpan">
            时间：{{ year }}<span class="blank15"></span>出版组织：{{ org }}
          </span>
        </p>
        <!--<p class="text">
          <span class="textSpan"> 时间：{{ year }} </span>
        </p>-->
      </el-row>
    </a>
    <!-- 第一个文章的pdf按钮-->
    <div id="u101">
      <el-button type="primary" class="RBtn" @click="toPdf(pdfUrl)"
        >PDF</el-button
      >
    </div>
    <!--第一个文章的code按钮-->
    <div id="u102">
      <el-button type="primary" class="RBtn" @click="toCode(codeUrl)"
        >Code</el-button
      >
    </div>
  </div>
</template>

<script>
export default {
  props: ["paper"],
  name: "resultItem",
  data() {
    return {}
  },
  computed: {
    title() {
      return this.paper.title
    },
    authors() {
      return this.paper.authors
    },
    abstract() {
      return this.paper.abstract
    },
    year() {
      return this.paper.year
    },
    org() {
      return this.paper.publicationOrg
    },
    pdfUrl() {
      return this.paper.pdfUrl
    },
    codeUrl() {
      return this.paper.codeUrl
    },
  },
  methods: {
    toDetail() {
      // this.$router.push({ name: "Detail", params: { id: this.paper._id } })
      let newpage = this.$router.resolve({
        name: "Detail",
        query: {
          id: this.paper._id,
        },
      })
      window.open(newpage.href, "_blank")
    },
    toPdf(url) {
      window.open(url, "_blank")
    },
    toCode(url) {
      window.open(url, "_blank")
    },
  },
}
</script>

<style>
.resultItemBox {
  margin: 15px 0 5px 0;
  border-width: 5px;
  position: relative;
  display: block;
  left: 20%;
  top: 0px;
  background-color: rgba(255, 255, 255, 1);
  border-radius: 0px;
  text-align: left;
  padding-left: 10%;
  height: 260px;
  box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.349019607843137);
}
.resultItemBox:hover {
  box-shadow: 5px 5px 9px rgba(0, 0, 0, 0.349019607843137);
}
.profileRow {
  margin-top: -9px;
}
span {
  font-family: "PingFangSC-Regular", "PingFang SC", sans-serif;
}

#titleRow {
  border-width: 0px;
  position: relative;
  left: 20px;
  width: 300px;
  height: 25px;
  display: flex;
}
.titleSpan {
  background-color: rgba(255, 255, 255, 0);
  color: #4a83e7;
  font-weight: 500;
  font-style: normal;
  font-size: 20px;
  word-break: normal;
  display: block;
  white-space: pre-wrap;
  word-wrap: break-word;
  overflow: hidden;
  width: 90%;
  word-break: break-all;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2; /* 这里是超出几行省略 */
  overflow: hidden;
}
.titile_text {
  max-width: 100%;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
.titleSpan:hover {
  text-decoration: underline;
}
.textSpan {
  background-color: rgba(255, 255, 255, 0);
  color: black;
  width: 80%;
  word-break: break-all;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 1; /* 这里是超出几行省略 */
  overflow: hidden;
}

.text1 {
  border-width: 0px;
  word-wrap: break-word;
  text-transform: none;
  background-color: rgba(255, 255, 255, 0);
  color: black;
  text-align: left;
  font-weight: 400;
}

.zhaiyao {
  width: 80%;
  word-break: break-all;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 4; /* 这里是超出几行省略 */
  overflow: hidden;
}
.text {
  border-width: 0px;
  word-wrap: break-word;
  text-transform: none;
  background-color: rgba(255, 255, 255, 0);
  color: black;
  text-align: left;
  font-weight: 400;
}
.RBtn {
  width: 100px;
}

span.blank15 {
  padding-left: 15px;
}
/*-------------------------101是pdf按钮的样式-------------*/
#u101 {
  border-width: 0px;
  position: absolute;
  left: 85%;
  top: 40%;
  width: 100px;
  height: 37px;
  display: flex;
}
/*-------------------------102是code按钮的样式-------------*/

#u102 {
  border-width: 0px;
  position: absolute;
  left: 85%;
  top: 65%;
  width: 100px;
  height: 37px;
  display: flex;
}
</style>