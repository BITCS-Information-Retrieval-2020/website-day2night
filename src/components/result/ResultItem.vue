<template>
  <a href="#" @click="toDetail" style="text-decoration: none">
    <div class="resultItemBox">
      <!-- {{ paper }} -->
      <!-- 第一个文章题目 -->
      <el-row class="titleRow">
        <p>
          <span class="titleSpan">{{ title }}</span>
        </p>
      </el-row>
      <!-- 第一个文章的作者、出版机构、时间 -->
      <el-row class="profileRow">
        <!--p class="text">
          <span> 摘要：{{ abstract }} </span>
        </!--p-->
        <p class="text">
          <span class="textSpan"> 作者：{{ authors }} </span>
        </p>
        <p class="text">
          <span class="textSpan"> 出版组织：{{ org }} </span>
        </p>
        <p class="text">
          <span class="textSpan"> 时间：{{ year }} </span>
        </p>
      </el-row>
      <!-- 第一个文章的pdf按钮-->
    <div id="u101" class="ax_default _图片_">
      <el-button type="primary" >PDF</el-button>
    </div>
    <!--第一个文章的code按钮-->
    <div id="u102" class="ax_default _图片_">
      <el-button type="primary" >Code</el-button>
    </div> 
    </div>
  </a>
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
  },
  methods: {
    toDetail() {
      //   alert(this.paper._id)
      this.$router.push({ name: "Detail", params: { id: this.paper._id } })
    },
  },
}
</script>

<style>
.resultItemBox {
  margin: 15px 0 5px 0;
  border-width:5px;
  position: relative;
  display:block;
  left: 200px;
  top:20px;
  width:850px;
  background-color:rgba(255, 255, 255, 1);
  border-radius:0px;
  text-align: left;
  padding-left: 10%;
  -moz-box-shadow:5px 5px 9px rgba(0, 0, 0, 0.349019607843137);
  -webkit-box-shadow:5px 5px 9px rgba(0, 0, 0, 0.349019607843137);
  box-shadow:5px 5px 9px rgba(0, 0, 0, 0.349019607843137);
}
.profileRow{
  margin-top: -9px;
}
span {
  font-family: "PingFangSC-Regular", "PingFang SC", sans-serif;
}

#titleRow{
  border-width:0px;
  position:relative;
  left: 20px;
  width:547px;
  height:25px;
  display:flex;

}
.titleSpan{
  background-color:rgba(255, 255, 255, 0);
  color:#4a83e7;
  font-weight: 600;
  font-style:normal;
  font-size:20px;
}

.textSpan{
    background-color:rgba(255, 255, 255, 0);
  color: black;

}

.text{
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
  background-color:rgba(255, 255, 255, 0);
  color: black;
  text-align:left;
  font-weight: 400;
  }
/*-------------------------101是pdf按钮的样式-------------*/
#u101 {
  border-width:0px;
  position:absolute;
  left:652px;
  top:70px;
  width:150px;
  height:37px;
  display:flex;
}
/*-------------------------102是code按钮的样式-------------*/

#u102 {
  border-width:0px;
  position:absolute;
  left:650px;
  top:120px;
  width:150px;
  height:37px;
  display:flex;
}</style>