<template>
  <el-container>
    <h-search-bar @searchResults="searchResults"></h-search-bar>
    <ol>
      <!-- <li v-for="(item, index) in hotList" :key="index">
        {{ item.title }}
        <img :src="item.image">
      </li> -->
    </ol>
    <el-container>
      <el-main>
        <el-row>
          <el-col :span="24">
            <el-tabs>
              <el-tab-pane label="热门论文" />
            </el-tabs>
            <v-indexVideo />
          </el-col>
        </el-row>
        <el-row class="marginLeft" :gutter="15">
          <el-col
            :span="4"
            v-for="(item, index) in hotList"
            :key="index"
            class="marginTop"
          >
            <el-card :body-style="{ padding: '0px' }" shadow="hover">
              <div class="videoDiv">
                <div class="coverDiv" @click="todo(item._id)">
                  <el-row>
                    <el-col :span="24">
                      <img :src="item.image" class="rightulliimg" />
                    </el-col>
                  </el-row>
                </div>
                <div class="videoMes">
                  <el-row>
                    <el-col :span="1" :offset="1"> </el-col>
                    <el-col :span="20" :offset="1" class="videoText">
                      <span class="text" :model="item.title">{{
                        item.title
                      }}</span>
                    </el-col>
                  </el-row>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </el-main>
      <!-- 侧边导航菜单 -->
      <!--  <el-aside width="400px">
        <p>热门论文表</p>
      </el-aside> -->
    </el-container>
    <el-footer>
      <p class="marginTop" @click="toAbout">关于我们</p>
      <p>&copy;2021 Paper Day2night</p>
    </el-footer>
  </el-container>
</template>

<script>
import HSearchBar from "components/home/HSearchBar"
//import IndexVideo from 'components/home/indexVideo.vue'
import { hotApi } from "request"

export default {
  name: "Home",
  components: {
    HSearchBar,
    //'v-indexVideo': IndexVideo,
  },
  data() {
    return {
      hotList: [],
    }
  },
  methods: {
    // 获取搜索结果
    searchResults(results) {
      // console.log(results)
      // result需要为列表类型
      this.$router.push({ name: "Result", params: { results: results } })
    },
    todo(id) {
      console.log("id")
      console.log(id)
      this.$router.push({ name: "Detail", params: { id: id } })
    },
    toAbout() {
      this.$router.push({ name: "About" })
    },
  },
  mounted() {
    let query = { num: 12 }
    hotApi(query)
      .then((res) => {
        console.log(res.data)
        this.hotList = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  },
}
</script>
  <style lang='scss' scoped>
.el-main {
  background-color: #fcfcfc;
  color: #333;
  text-align: center;
  line-height: 30px;
}
.el-aside {
  background-color: #ffffff;
  color: #333;
  text-align: center;
  line-height: 30px;
}
.el-footer {
  height: 100px;
  background-color: #14161a;
  color: rgb(255, 255, 255);
  text-align: center;
  line-height: 10px;
}
.coverDiv {
  width: 100%;
  height: 150px;
  background: #f2f2f2;
  display: flex;
  justify-content: center;
  align-items: center;
  .rightulliimg {
    width: 100%;
    height: 150px;
  }
}
.videoText {
  margin-top: 3px;
  color: black;
  font-size: 8px;
  .text {
    float: left;
  }
}
.hotlist {
  margin-left: 6%;
}
.videoDiv {
  width: 100%;
  height: 230px;
  float: left;
}
.titleText {
  font-size: 30px;
}
.coverSwiperDiv {
  width: 100%;
  height: 350px;
  background: #f2f2f2;
  display: flex;
  justify-content: center;
  align-items: center;
  .rightSwiperulliimg {
    width: 100%;
    max-height: 350px;
  }
}
.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}
.marginLeft {
  margin-left: 6%;
}
.marginTop {
  margin-top: 15px;
}
.marginTop2 {
  margin-top: 10px;
}
.marginRight {
  margin-right: 40px;
}
.marginRight2 {
  margin-right: 2%;
}
.videoMes {
  margin-top: 8px;
}
.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}

.mySvideo {
  width: 80%;
  margin-left: 5%;
}
.myvideo2 {
  float: right;
  width: 100%;
  margin-left: 5%;
}
</style>