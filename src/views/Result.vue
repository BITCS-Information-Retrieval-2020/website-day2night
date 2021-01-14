<template>
  <div>
    <search-bar @searchResults="searchResults"></search-bar>
    <!-- {{ results }} -->
    <!-- {{ totalPage }} -->
    <!-- {{ currentQuery }} -->

    <el-row id="main">
      <el-col id="side" :span="5" style="background-color: red">
        <el-row id="orgList">
          <p><span class="titlet">来源</span></p>
          <p v-for="(org, index) in orgList" :key="index">
            <a class="listItem" href="#" @click="slectByOrg">{{ org }}</a>
          </p>
        </el-row>
        <el-row id="yearList">
          <p><span class="titlet">年度</span></p>
          <p v-for="(year, index) in yearList" :key="index">
            <a class="listItem" href="#" @click="selectByYear">{{ year }}</a>
          </p>
        </el-row>
      </el-col>
      <el-col id="resultList" :span="19">
        <result-item
          v-for="(paper, index) in results"
          :key="index"
          :paper="paper"
        ></result-item>
        <el-pagination
          layout="prev, pager, next"
          :total="totalPage"
          @prev-click="prevClick"
          @next-click="nextClick"
          @current-change="currentChange"
        >
        </el-pagination>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import SearchBar from "common/SearchBar.vue"
import ResultItem from "components/result/ResultItem.vue"
import { searchByKeywordApi } from "request"

export default {
  components: { SearchBar, ResultItem },
  name: "Result",
  data() {
    return {
      results: [],
      currentQuery: {},
      totalPage: 0,

      orgList: ["aaaa", "bbbbb", "ccccc", "ddddd", "eeeeee"],
      yearList: ["2020", "2019", "2018", "2017"],
    }
  },
  methods: {
    selectByYear() {},
    slectByOrg() {},
    // 获取搜索结果
    searchResults(results) {
      // console.log(results)
      this.results = results.results
      this.totalPage = results.totalPage
      this.currentQuery = results.query
    },
    prevClick() {
      let query = this.currentQuery
      query.page -= 1
      this.sendSearch(query)
    },
    nextClick() {
      let query = this.currentQuery
      query.page += 1
      this.sendSearch(query)
    },
    currentChange(page) {
      // console.log(page)
      let query = this.currentQuery
      query.page = page
      this.sendSearch(query)
    },
    sendSearch(query) {
      searchByKeywordApi(query)
        .then((res) => {
          // console.log(res.data)
          this.results = res.data.resultData
          this.totalPage = res.data.totalPage
          this.currentQuery = query
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
  mounted() {
    //获取搜索结果
    this.results = this.$route.params.results.results
    this.currentQuery = this.$route.params.results.query
    this.totalPage = this.$route.params.results.totalPage
  },
}
</script>

<style>
a {
  text-decoration: none;
}
#main {
  background-color: blue;
}
#side {
}
#orgList {
}
.titlet {
}
.listItem {
}
</style>