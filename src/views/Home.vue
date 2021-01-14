<template>
  <div>
    <h-search-bar @searchResults="searchResults"></h-search-bar>
    <p>热门论文表</p>
    <ol>
      <li v-for="(item, index) in hotList" :key="index">{{ item.title }}</li>
    </ol>
  </div>
</template>

<script>
import HSearchBar from "components/home/HSearchBar"
import { hotApi } from "request"

export default {
  name: "Home",
  components: {
    HSearchBar,
  },
  data() {
    return {
      hotList: [],
    }
  },
  methods: {
    // 获取搜索结果
    searchResults(results) {
      // console.log(results)
      // result需要为列表类型
      this.$router.push({ name: "Result", params: { results: results } })
    },
  },
  mounted() {
    let query = { num: 10 }
    hotApi(query)
      .then((res) => {
        // console.log(res.data)
        this.hotList = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  },
}
</script>

<style>
</style>
