<template>
  <div>
    <search-bar @searchResults="searchResults"></search-bar>
    <!-- {{ results }} -->
    <!-- {{ totalNum }} -->
    <!-- {{ currentQuery }} -->

    <el-row id="main">
      <el-col id="side" :span="5">
        <el-row id="orgList">
          <p><span class="titlet">来源</span></p>
          <p v-for="(org, index) in orgList" :key="index">
            <a class="listItem" href="#" @click="slectByOrg(org)">{{ org }}</a>
          </p>
        </el-row>
        <el-row id="yearList">
          <p><span class="titlet">年度</span></p>
          <p v-for="(year, index) in yearList" :key="index">
            <a class="listItem" href="#" @click="selectByYear(year)">{{
              year
            }}</a>
          </p>
        </el-row>
      </el-col>
      <el-col id="resultList" :span="19">
        <result-item
          v-for="(paper, index) in results"
          :key="index"
          :paper="paper"
        ></result-item>
        </el-col>
        <el-pagination
          layout="total,prev, pager, next"
          :total="totalNum"
          :page-size="8"
          @prev-click="prevClick"
          @next-click="nextClick"
          @current-change="currentChange"
        >
        </el-pagination>
      
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
      results: [], //用于展示的数据
      results_raw: [], //请求到的原始数据
      results_select: [], //经过筛选的数据
      currentQuery: {},
      totalNum: 0,
      currentPage: 1,

      orgList: ["aaaa", "bbbbb", "ccccc", "ddddd", "eeeeee"],
      yearList: ["2020", "2019", "2018", "2017"],
    }
  },
  methods: {
    selectByYear(year) {
      this.results_select = this.results_raw.filter((item) => {
        return Number(item.year) == Number(year)
      })
      // console.log(this.results_select)
    },
    slectByOrg(org) {
      // console.log(org)
      let selectList = this.results_raw.filter((item) => {
        // console.log(item.publicationOrg == org)
        return item.publicationOrg == org
      })
      // console.log(selectList)
      this.results_select = selectList
    },
    // 获取搜索结果
    searchResults(results) {
      // console.log(results)
      this.results_raw = results.results
      this.getYearList(this.results_raw)
      this.getOrgList(this.results_raw)
      this.totalNum = results.totalNum
      this.currentQuery = results.query
    },
    prevClick() {
      this.currentPage -= 1
      this.sliceResults_select(this.currentPage)
      // let query = this.currentQuery
      // query.page -= 1
      // this.sendSearch(query)
    },
    nextClick() {
      this.currentPage += 1
      this.sliceResults_select(this.currentPage)
      // let query = this.currentQuery
      // query.page += 1
      // this.sendSearch(query)
    },
    currentChange(page) {
      this.sliceResults_select(page)
      // console.log(page)
      // let query = this.currentQuery
      // query.page = page
      // this.sendSearch(query)
    },
    sendSearch(query) {
      searchByKeywordApi(query)
        .then((res) => {
          // console.log(res.data)
          this.results = res.data.resultData
          this.totalNum = res.data.totalNum
          this.currentQuery = query
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getYearList(results) {
      let years = []
      for (let item of results) {
        if (years.indexOf(item.year) == -1) {
          years.push(item.year)
        }
      }
      // console.log(years)
      this.yearList = years.sort().reverse()
    },
    getOrgList(results) {
      let orgs = []
      for (let item of results) {
        if (orgs.indexOf(item.publicationOrg) == -1) {
          orgs.push(item.publicationOrg)
        }
      }
      // console.log(orgs)
      this.orgList = orgs
    },
    sliceResults_select(page) {
      let start = (page - 1) * 8
      this.results = this.results_select.slice(start, 8 + start)
    },
  },
  watch: {
    results_select() {
      this.totalNum = this.results_select.length
      this.currentPage = 1
      this.sliceResults_select(this.currentPage)
    },
    results_raw() {
      this.results_select = this.results_raw
    },
  },
  mounted() {
    //获取搜索结果
    this.results_raw = this.$route.params.results.results
    this.currentQuery = this.$route.params.results.query
    this.totalNum = this.$route.params.results.totalNum
    this.getYearList(this.results_raw)
    this.getOrgList(this.results_raw)
    this.results_select = this.results_raw
    this.results = this.results_raw
  },
}
</script>

<style>
a {
  text-decoration: none;
}
#main {
    background-color:rgba(242, 242, 242, 1);
}
#side {
  top:10px;
  position:absolute;
  left:50px;
  text-align:left;

}

.titlet {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
  background-color:rgba(255, 255, 255, 0);
  text-align:left;
  font-weight: 600;
  font-size: 18px;

}

.listItem {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
  background-color:rgba(255, 255, 255, 0);
  color: black;
  text-align:left;
  font-weight: 500;
}
.el-pagination{
  position: absolute;
  bottom: 0px;
  display:block ;
  text-align: center;
  height: 30px;
  width: 100%;

}
</style>