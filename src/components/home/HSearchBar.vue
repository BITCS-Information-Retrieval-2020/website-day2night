<template>
  <el-row id="HsearchBar">
    <el-row id="HlogoCol">
      <el-col :span="2" :offset="7"><i class="el-icon-search"></i></el-col>
      <el-col :span="12">
        <p>Paper Day2night</p>
      </el-col>
    </el-row>
    <el-row id="HinputCol">
      <el-row id="HinputBox">
        <el-col :span="20">
          <el-autocomplete
            class="Hinline-input"
            id="Hinput"
            placeholder="请输入检索关键字"
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
                <el-button slot="reference" type="text" id="HadvancedBtn"
                  >高级检索</el-button
                >
              </el-popover>
            </template>
          </el-autocomplete>
        </el-col>
        <el-col :span="4" style="margin: 0px">
          <el-button id="HsearchBtn" @click="search">
            <span id="HsearchText">
              <i class="el-icon-search" style="margin-right: 15px"></i>搜索
            </span>
          </el-button>
        </el-col>
      </el-row>
      <el-row id="HcheckBox">
        <el-checkbox-group v-model="checkedList">
          <el-checkbox
            class="HcheckItem"
            v-for="option in checkList"
            :label="option"
            :key="option"
            >{{ option }}</el-checkbox
          >
        </el-checkbox-group>
      </el-row>
    </el-row>
  </el-row>
</template>

<script>
import AdvancedSearch from "common/AdvancedSearch.vue"
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
      advancedSearchForm: {},
    }
  },
  methods: {
    //搜索功能
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
          operator[0] = "OR"
          tempQuery.titile = this.input
        }
        if (this.checkedList.indexOf("作者") > -1) {
          operator[1] = "OR"
          tempQuery.author = this.input
        }
        if (this.checkedList.indexOf("摘要") > -1) {
          operator[2] = "OR"
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
          console.log(res.data)
          let results = {
            results: res.data.resultData,
            query: query,
            totalPage: res.data.totalPage,
          }
          this.$emit("searchResults", results)
        })
        .catch((error) => {
          console.log(error)
        })
    },

    advancedSearch(form) {
      console.log(form)
      let query = {
        type: "1",
        page: "1",
        query: form,
      }
      this.sendSearch(query)
    },

    //以下都是搜索补全
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
#HlogoCol {
  padding-block: 15px;
}
#HlogoCol p {
  color: white;
  text-align: left;
  margin: 0;
  font-size: 45px;
  font-weight: 800;
}
#HlogoCol i {
  color: white;
  text-align: right;
  margin: 0;
  font-size: 60px;
  font-weight: 900;
}
#HsearchBar {
  background-color: #4a84e8f2;
  height: 300px;
  padding-top: 30px;
}
#HinputCol {
  background-color: #234173f1;
  width: 80%;
  margin-left: 10%;
  padding: 25px 30px 10px 30px;
  height: 130px;
  border-radius: 15px;
}
#HinputBox {
  margin-bottom: 20px;
}
#Hinput {
  height: 50px;
  font-size: 18px;
}
.Hinline-input {
  width: 100%;
}
.el-input .el-input__count {
  align-items: baseline !important;
}
#HadvancedBtn {
  font-size: 18px;
  padding-inline: 10px;
  color: #4a84e8f2;
}
#HadvancedBtn:hover {
  background-color: #edf2fcf2;
}
#HsearchBtn {
  width: 100%;
  height: 50px;
  background-color: #4a84e8f2;
  border-radius: 5px;
}
#HsearchText {
  color: white;
  font-size: 22px;
}
.HcheckItem > .el-checkbox__label {
  font-size: 16px;
}
.HcheckItem {
  color: white;
}
</style>
