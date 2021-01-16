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
  <el-row style="margin-left: 10%;width: 70%;margin-bottom: 30px">
    <el-row>
      <p id="title">论文预览</p>
    </el-row>
    <el-row >
      <div>
        <button @click="changePdfPage(0)">上一页</button>
        第{{page}}页/共{{pagenum}}页
        <button @click="changePdfPage(1)">下一页</button>
      </div>
    </el-row>
    <el-row>
      <div id="display" class="pdf">
        <pdf
          ref="pdf"
          :page = "page"
          :src="pdfUrl"
          @num-pages="pagenum=$event">
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
#title{
  text-align: left;
  margin-top: 30px
}

#display{

}
</style>