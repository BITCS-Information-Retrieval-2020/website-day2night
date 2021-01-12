<template>
  <h-search-bar @searchResults="searchResults"></h-search-bar>
</template>

<script>
import HSearchBar from "components/home/HSearchBar"
export default {
  name: "Home",
  components: {
    HSearchBar,
  },
  data() {
    return {}
  },
  methods: {
    // 获取搜索结果
    searchResults(results) {
      console.log(results)
      // result需要为列表类型
      this.$router.push({ name: "Result", params: { results: results } })
    },
  },
}
</script>

<style>
</style>
