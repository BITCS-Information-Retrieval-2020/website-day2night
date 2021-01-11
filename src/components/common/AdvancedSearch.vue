<template>
  <el-form id="AdForm" :model="form" label-width="80px">
    <el-form-item label="标题">
      <el-input></el-input>
    </el-form-item>
    <el-form-item label="作者">
      <el-input></el-input>
    </el-form-item>
    <el-form-item label="摘要">
      <el-input></el-input>
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
      },
    }
  },
  methods: {
    onSubmit() {
      console.log(this.form)
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