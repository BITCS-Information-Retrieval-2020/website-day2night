<template>
  <el-row id="searchBar">
    <el-col id="logoCol" :span="6" @click="toHome">
      <el-col :span="10"><i class="el-icon-search"></i></el-col>
      <el-col :span="12">
        <p>Paper</p>
        <p>Day2night</p>
      </el-col>
    </el-col>
    <el-col id="inputCol" :span="16">
      <el-row id="inputBox">
        <el-col :span="20">
          <el-autocomplete
            class="inline-input"
            id="input"
            v-model="input"
            :maxlength="200"
            show-word-limit
            :fetch-suggestions="querySearch"
            :trigger-on-focus="false"
            @select="handleSelect"
          >
            <template slot="prepend">
              <el-popover placement="bottom-start" trigger="click">
                <advanced-search
                  @advancedSearch="advancedSearch"
                ></advanced-search>
                <el-button slot="reference" type="text" id="advancedBtn"
                  >高级检索</el-button
                >
              </el-popover>
            </template>
          </el-autocomplete>
        </el-col>
        <el-col :span="4" style="margin: 0px">
          <el-button id="searchBtn" @click="search">
            <span id="searchText">
              <i class="el-icon-search" style="margin-right: 15px"></i>搜索
            </span>
          </el-button>
        </el-col>
      </el-row>
      <el-row id="checkBox">
        <el-checkbox-group v-model="checkedList">
          <el-checkbox
            class="checkItem"
            v-for="option in checkList"
            :label="option"
            :key="option"
            >{{ option }}</el-checkbox
          >
        </el-checkbox-group>
      </el-row>
    </el-col>
  </el-row>
</template>

<script>
import AdvancedSearch from "./AdvancedSearch.vue"
import { searchByKeywordApi, searchSuggestApi } from "request"

const checkOptions = ["标题", "作者", "摘要"]
export default {
  components: { AdvancedSearch },
  name: "SearchBar",
  data() {
    return {
      input: "",
      checkedList: checkOptions,
      checkList: checkOptions,
    }
  },
  methods: {
    toHome() {
      this.$router.push({ name: "Home" })
    },
    search() {
      let query = {
        type: "",
        page: "1",
      }
      if (this.checkedList.length == this.checkList.length) {
        query.type = "0"
        query.query = this.input
        console.log(query)
      } else {
        let operator = ["", "", "", ""]
        let tempQuery = {
          titile: "",
          author: "",
          abstract: "",
          content: "",
        }
        if (this.checkedList.indexOf("标题") > -1) {
          operator[0] = "AND"
          tempQuery.titile = this.input
        }
        if (this.checkedList.indexOf("作者") > -1) {
          operator[1] = "AND"
          tempQuery.author = this.input
        }
        if (this.checkedList.indexOf("摘要") > -1) {
          operator[2] = "AND"
          tempQuery.abstract = this.input
        }
        tempQuery.operator = operator
        query.type = "1"
        query.query = tempQuery
        // console.log(query)
      }
      this.sendSearch(query)
    },
    sendSearch(query) {
      searchByKeywordApi(query)
        .then((res) => {
          // console.log(res.data)
          let results = {
            results: res.data.resultData,
            query: query,
            totalNum: res.data.totalNum,
          }
          this.$emit("searchResults", results)
        })
        .catch((error) => {
          console.log(error)
        })
    },

    advancedSearch(form) {
      let query = {
        type: "1",
        page: "1",
        query: form,
      }
      this.sendSearch(query)
    },

    handleSelect(item) {
      console.log(item)
    },
    querySearch(queryString, cb) {
      searchSuggestApi(queryString)
        .then((res) => {
          // console.log(res.data)
          let suggestionsList = res.data.resultData
          // console.log(suggestions)
          let suggestions = []
          for (let item of suggestionsList) {
            let suggob = { value: item }
            suggestions.push(suggob)
          }
          cb(suggestions)
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
}
</script>

<style>
#logoCol {
  padding-block: 15px;
  margin-right: 20px;
}
#logoCol p {
  color: white;
  text-align: left;
  margin: 0;
  font-size: 40px;
}
#logoCol i {
  color: white;
  margin: 0;
  font-size: 90px;
  font-weight: 900;
}
#searchBar {
  background-color: #4a84e8f2;
  height: 130px;
  padding: 5px;
}
#inputCol {
  background-color: #234173f1;
  margin-block: 0px;
  padding: 20px 20px 10px 10px;
  height: 100%;
  border-radius: 0 15px 15px 0;
}
#inputBox {
  margin-bottom: 20px;
}
#input {
  height: 50px;
  font-size: 18px;
}
.inline-input {
  width: 100%;
}
.el-input .el-input__count {
  align-items: baseline;
}
#advancedBtn {
  font-size: 18px;
  padding-inline: 10px;
  color: #4a84e8f2;
}
#advancedBtn:hover {
  background-color: #edf2fcf2;
}
#searchBtn {
  width: 100%;
  height: 50px;
  background-color: #4a84e8f2;
  border-radius: 0 15px 15px 0;
}
#searchText {
  color: white;
  font-size: 22px;
}
.checkItem > .el-checkbox__label {
  font-size: 16px;
}
.checkItem {
  color: white;
}
</style>
