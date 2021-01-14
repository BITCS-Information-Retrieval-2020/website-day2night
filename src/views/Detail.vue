<template>
  <div>
    <search-bar @searchResults="searchResults"></search-bar>
  </div>
</template>

<script>
import SearchBar from "common/SearchBar"
export default {
  name: "Detail",
  components: {
    SearchBar,
  },
  data() {
    return {}
  },
  methods: {
    // 获取搜索结果
    searchResults(results) {
      console.log(results)
      this.$router.push({ name: "Result", params: { results: results } })
    },
  },
}
</script>

<style>
</style>