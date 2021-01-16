<template>
  <el-row id="pdfbox" >
    <el-row>
      <h2 id="title">论文预览</h2>
    </el-row>
    <el-row >
      <div>
        <el-button type="text" style="padding-right: 10px;" @click="changePdfPage(0)">上一页</el-button>
        第{{page}}页/共{{pagenum}}页
        <el-button type="text" @click="changePdfPage(1)">下一页</el-button>
      </div>
    </el-row>
    <el-row>
      <div id="display" class="pdf">
        <pdf
          ref="pdf"
          :page = "page"
          :src="pdfUrl"
          @num-pages="pagenum=$event"
          style=" border:double">
        </pdf>
      </div>
    </el-row>
  </el-row>
</template>

<script>
import pdf from 'vue-pdf'
export default {
  name: 'Pdf',
  components: {
    pdf
  },
  props:["detail"],
  data: function () {
    return {
      page: 1,
      pagenum:0,
    }
  },
  methods: {
    changePdfPage(val) {
      if (val === 0 && this.page > 1) {
        this.page--;
        // console.log(this.page)
      }
      if (val === 1 && this.page<this.pagenum) {
        this.page++;
        // console.log(this.page)
      }
    },
  },
  computed:{
    pdfUrl() {
      console.log(this.detail.pdfPath)
      return this.detail.pdfPath
    },
  }
}
</script>

<style scoped>
#pdfbox{
  margin-left: 7%;
  width: 75%;
  margin-bottom: 30px;
  box-shadow:3px 3px 5px 0px #787878;
  background-color: #ffffff

}
#title{
  padding-left: 20px;
  text-align: left;
  margin-top: 30px;
  color: #4a83e7;
}
#display{
  padding-left: 5%;
  padding-right: 5%;
  margin-top: 3px;
  margin-bottom: 3%;

}
</style>