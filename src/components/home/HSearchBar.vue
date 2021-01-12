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
            maxlength="200"
            show-word-limit
            :fetch-suggestions="querySearch"
            :trigger-on-focus="false"
            @select="handleSelect"
          >
            <template slot="prepend">
              <el-popover placement="bottom-start" trigger="click">
                <advanced-search></advanced-search>
                <el-button slot="reference" type="text" id="HadvancedBtn"
                  >高级检索</el-button
                >
              </el-popover>
            </template>
          </el-autocomplete>
        </el-col>
        <el-col :span="4" style="margin: 0px">
          <el-button id="HsearchBtn">
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
#HlogoCol {
  padding-block: 15px;
}
#HlogoCol p {
  color: white;
  text-align: left;
  margin: 0;
  font-size: 40px;
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
  align-items: baseline;
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
