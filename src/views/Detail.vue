<template>
  <search-bar @searchResults="searchResults"></search-bar>
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
    },
  },
}
</script>

<style>
</style>