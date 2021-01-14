<template>
  <div>
    <search-bar @searchResults="searchResults"></search-bar>
    {{ results }}
    <!-- 这部分写html代码 -->

    <!--  -->
    <el-pagination
      layout="prev, pager, next"
      :total="totalPage"
      :pager-count="11"
      @prev-click="prevClick"
      @next-click="nextClick"
      @current-change="currentChange"
    >
    </el-pagination>
  </div>
</template>

<script>
import SearchBar from "common/SearchBar.vue"
import { searchByKeywordApi } from "request"
export default {
  components: { SearchBar },
  name: "Result",
  data() {
    return {
      results: [],
      currentQuery: {},
      totalPage: 1,
    }
  },
  methods: {
    // 获取搜索结果
    searchResults(results) {
      // console.log(results)
      this.results = results.results
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
      console.log(page)
      let query = this.currentQuery
      query.page = page
      this.sendSearch(query)
    },
    sendSearch(query) {
      searchByKeywordApi(query)
        .then((res) => {
          // console.log(res.data)
          this.results = res.data.rasultData
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
/* 这部分写css代码 */

/*  */
</style>