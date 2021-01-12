<template>
  <search-bar @searchResults="searchResults"></search-bar>
  <!-- 这部分写html代码 -->

  <!--  -->
</template>

<script>
import SearchBar from "common/SearchBar.vue"
export default {
  components: { SearchBar },
  name: "Result",
  data() {
    return {
      results: [],
    }
  },
  methods: {
    // 获取搜索结果
    searchResults(results) {
      console.log(results)
    },
  },
  mounted() {
    //获取搜索结果
    this.results = this.$route.params.results
  },
}
</script>

<style>
/* 这部分写css代码 */

/*  */
</style>