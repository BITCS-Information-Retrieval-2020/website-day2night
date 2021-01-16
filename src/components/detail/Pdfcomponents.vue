<!--<template>-->
<!--  <div class="pdf" v-show="fileType === 'pdf'">-->
<!--    <p class="arrow">-->
<!--      <span @click="changePdfPage(0)" class="turn" :class="{grey: currentPage==1}">Preview</span>-->
<!--      {{ currentPage }}/{{ pageCount }}-->
<!--      <span-->
<!--        @click="changePdfPage(1)"-->
<!--        class="turn"-->
<!--        :class="{ grey: currentPage == pageCount }"-->
<!--      >Next</span>-->
<!--    </p>-->
<!--    <pdf-->
<!--      :src="src"-->
<!--      :page="currentPage"-->
<!--      @num-pages="pageCount = $event"-->
<!--      @page-loaded="currentPage = $event"-->
<!--      @loaded="loadPdfHandler">-->
<!--    </pdf>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import pdf from 'vue-pdf'-->
<!--export default {-->
<!--  name: "Pdfcomponents",-->
<!--  components: {pdf},-->
<!--  data() {-->
<!--    return {-->
<!--      currentPage: 0, // pdf文件页码-->
<!--      pageCount: 0, // pdf文件总页数-->
<!--      fileType: "pdf", //文件类型-->
<!--      src: "file:///D:/BIT/Information_retrieval/Talk1-Introduction-mxl.pdf" // pdf文件地址-->
<!--    }-->
<!--  },-->
<!--  created: {-->
<!--    //this.src = pdf.createLoadingTask(this.src)-->
<!--  },-->
<!--  method: {-->
<!--    // 改变PDF页码,val传过来区分上一页下一页的值,0上一页,1下一页-->
<!--    changePdfPage(val) {-->
<!--      // console.log(val)-->
<!--      if (val === 0 && this.currentPage > 1) {-->
<!--        this.currentPage&#45;&#45;;-->
<!--        // console.log(this.currentPage)-->
<!--      }-->
<!--      if (val === 1 && this.currentPage < this.pageCount) {-->
<!--        this.currentPage++;-->
<!--        // console.log(this.currentPage)-->
<!--      }-->
<!--    },-->

<!--    // pdf加载时-->
<!--    loadPdfHandler(e) {-->
<!--      this.currentPage = 1; // 加载的时候先加载第一页-->
<!--    }-->
<!--  }-->
<!--};-->
<!--</script>-->

<!--<style scoped>-->
<!--</style>-->

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
  data: function () {
    return {
      pdfUrl: "/abc.pdf",
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
  }
}
</script>

<style scoped>
#pdfbox{
  margin-left: 5%;
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