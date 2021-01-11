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
          <el-autocomplete
            class="inline-input"
            id="input"
            v-model="input"
            maxlength="200"
            show-word-limit
            :fetch-suggestions="querySearch"
            :trigger-on-focus="false"
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
          </el-autocomplete>
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

const checkOptions = ["标题", "作者", "摘要"]
export default {
  components: { AdvancedSearch },
  name: "SearchBar",
  data() {
    return {
      input: "",
      checkedList: checkOptions,
      checkList: checkOptions,

      inputAdvices: [
        { value: "三全鲜食（北新泾店）", address: "长宁区新渔路144号" },
        {
          value: "Hot honey 首尔炸鸡（仙霞路）",
          address: "上海市长宁区淞虹路661号",
        },
        {
          value: "新旺角茶餐厅",
          address: "上海市普陀区真北路988号创邑金沙谷6号楼113",
        },
        { value: "泷千家(天山西路店)", address: "天山西路438号" },
        {
          value: "胖仙女纸杯蛋糕（上海凌空店）",
          address: "上海市长宁区金钟路968号1幢18号楼一层商铺18-101",
        },
        { value: "贡茶", address: "上海市长宁区金钟路633号" },
        {
          value: "豪大大香鸡排超级奶爸",
          address: "上海市嘉定区曹安公路曹安路1685号",
        },
        {
          value: "茶芝兰（奶茶，手抓饼）",
          address: "上海市普陀区同普路1435号",
        },
      ],
    }
  },
  methods: {
    handleSelect(item) {
      console.log(item)
    },
    querySearch(queryString, cb) {
      let restaurants = this.inputAdvices
      let results = queryString
        ? restaurants.filter(this.createFilter(queryString))
        : restaurants
      // 调用 callback 返回建议列表的数据
      cb(results)
    },
    createFilter(queryString) {
      return (restaurant) => {
        return (
          restaurant.value.toLowerCase().indexOf(queryString.toLowerCase()) ===
          0
        )
      }
    },
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
