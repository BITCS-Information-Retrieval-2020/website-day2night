<template>
  <el-form id="AdForm" :model="form" label-width="80px">
    <el-form-item label="标题">
      <el-input v-model="form.title"></el-input>
    </el-form-item>
    <el-form-item label="作者">
      <el-input v-model="form.author"></el-input>
    </el-form-item>
    <el-form-item label="摘要">
      <el-input v-model="form.abstract"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button id="subBtn" @click="onSubmit">搜索</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
export default {
  name: "AdvancedSearch",
  data() {
    return {
      form: {
        title: "",
        author: "",
        abstract: "",
        operater: ["", "", "", ""],
      },
    }
  },
  methods: {
    onSubmit() {
      // console.log(this.form)
      if (this.form.title != "") {
        this.form.operater[0] = "AND"
      }
      if (this.form.author != "") {
        this.form.operater[0] = "AND"
      }
      if (this.form.abstract != "") {
        this.form.operater[0] = "AND"
      }
      this.$emit("advancedSearch", this.form)
    },
  },
}
</script>

<style>
#AdForm {
  padding-right: 50px;
}
#subBtn {
  color: #4a84e8f2;
}
#subBtn:hover {
  background-color: #edf2fcf2;
}
</style>