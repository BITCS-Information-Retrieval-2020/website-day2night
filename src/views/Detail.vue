<template>
  <div id="container">
    <search-bar @searchResults="searchResults"></search-bar>

    <introducton :detail="detail"></introducton>
    <Pdf></Pdf>
  </div>
</template>

<script>
import SearchBar from "common/SearchBar"
import introducton from "components/detail/introducton"
import { detailApi } from "request"
import Pdf from "components/detail/Pdfcomponents";
export default {
  name: "Detail",
  components: {
    Pdf,
    SearchBar,
    introducton,

  },
  data() {
    return {
      detail: {},
    }
  },
  methods: {
    // 获取搜索结果
    searchResults(results){
      console.log(results)
      this.$router.push({ name: "Result", params: { results: results } })
    },
  },
  mounted() {
    let id = this.$route.params.id
    let query = { id: id }
    detailApi(query)
      .then((res) => {
        this.detail = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  },
}
</script>

<style>
#container {
  background-color: #f0f0f0;
  height: 100%;
}
</style>