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
        <p class="text">
          <span> 摘要：{{ abstract }} </span>
        </p>
        <p class="text">
          <span> 作者：{{ authors }} </span>
        </p>
        <p class="text">
          <span> 出版组织：{{ org }} </span>
        </p>
        <p class="text">
          <span> 时间：{{ year }} </span>
        </p>
      </el-row>
      <!-- 第一个文章的pdf按钮
    <div id="u101" class="ax_default _图片_">
      <el-button type="primary" round>PDF</el-button>
    </div>
    第一个文章的code按钮
    <div id="u102" class="ax_default _图片_">
      <el-button type="primary" round>Code</el-button>
    </div> -->
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
  background-color: blueviolet;
  margin: 5px 0 5px 0;
}
span {
  font-family: "PingFangSC-Regular", "PingFang SC", sans-serif;
}
</style>