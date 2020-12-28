<template>
  <el-row id="searchBar">
    <el-col id="logoCol" :span="6">
      <el-col :span="10"><i class="el-icon-search"></i></el-col>
      <el-col :span="12">
        <p>Paper</p>
        <p>Day2night</p>
      </el-col>
    </el-col>
    <el-col id="inputCol" :span="16">
      <el-row id="inputBox">
        <el-col :span="20">
          <el-input
            id="input"
            v-model="input"
            maxlength="200"
            show-word-limit
            :fetch-suggestions="querySearch"
            :trigger-on-focus="true"
            @select="handleSelect"
          >
            <template slot="prepend">
              <el-popover placement="bottom-start" trigger="click">
                <advanced-search></advanced-search>
                <el-button slot="reference" type="text" id="advancedBtn"
                  >高级检索</el-button
                >
              </el-popover>
            </template>
          </el-input>
        </el-col>
        <el-col :span="4" style="margin: 0px">
          <el-button id="searchBtn">
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

const checkOptions = ["标题", "作者", "摘要", "关键词"]
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
}
</script>

<style>
#logoCol {
  padding-block: 15px;
}
#logoCol p {
  color: white;
  text-align: left;
  margin: 0;
  font-size: 40px;
}
#logoCol i {
  color: white;
  text-align: left;
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
.el-input .el-input__count {
  align-items: baseline;
}
#advancedBtn {
  font-size: 18px;
  padding-inline: 10px;
  color: #4a84e8f2;
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
