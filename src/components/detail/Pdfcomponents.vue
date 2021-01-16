<template>
  <el-row id="pdfbox">
    <el-row>
      <h2 id="title">论文预览</h2>
    </el-row>
    <el-row v-if="this.pdfUrl.length==0" style="text-align: left; padding-left: 50px">
      <p style="margin-top: 1px">无论文</p>
    </el-row>
    <el-row v-if="this.pdfUrl.length>0">
      <div>
        <el-button type="text" style="padding-right: 10px;" @click="changePdfPage(0)">上一页</el-button>
        第{{page}}页/共{{pagenum}}页
        <el-button type="text" @click="changePdfPage(1)">下一页</el-button>
      </div>
    </el-row>
    <el-row v-if="this.pdfUrl.length>0">
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
    <el-row id="downBtn" v-if="this.pdfUrl.length>0">
      <el-button  type="text"  @click="download"><span class="el-icon-download" style="font-size:20px;"></span></el-button>
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
    download(){
      window.location.href = this.detail.pdfPath
    },
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
  margin-bottom: 3%
}
#downBtn {
  height: 50px;
  width: 50px;
}
</style>