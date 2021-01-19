<template>
  <el-row id="videobox" >
    <el-row>
      <h2 id="title">视频播放</h2>
    </el-row>
    <el-row  style="text-align: left; padding-left: 50px">
      <p v-if="this.detail.videoPath.length<=0" style="margin-top: 1px">无视频</p>
    </el-row>
    <el-row class='demo' v-if="this.detail.videoPath.length>0">
      <video-player class="video-player vjs-custom-skin"
                  ref="videoPlayer"
                  :playsinline="true"
                  :options="playerOptions">
<!--                  @play="onPlayerPlay($event)"-->
<!--                  @pause="onPlayerPause($event)"-->
<!--                  @canplay="onPlayerCanplay($event)"-->
<!--                  @canplaythrough="onPlayerCanplaythrough($event)"-->
<!--                  @statechanged="playerStateChanged($event)"-->
<!--                  @ready="playerReadied"-->
<!--    >-->
      </video-player>
    </el-row>
    <el-row id="downBtn" v-if="this.detail.videoPath.length>0">
<!--      {{this.playerOptions.sources[0].src}}-->
      <el-button  type="text"  @click="download"><span class="el-icon-download" style="font-size:20px;"></span></el-button>
    </el-row>
  </el-row>
</template>

<script>
import { videoPlayer } from 'vue-video-player'
import 'video.js/dist/video-js.css'
export default {
  name: "videocomponent",
  props:["detail"],
  components: {
    videoPlayer
  },
  data: function () {
    return {
      playerOptions: {
        playbackRates: [0.5, 1.0, 1.5, 2.0], // 可选的播放速度
        autoplay: false, // 如果为true,浏览器准备好时开始回放。
        muted: false, // 默认情况下将会消除任何音频。
        loop: false, // 是否视频一结束就重新开始。
        preload: 'auto', // 建议浏览器在<video>加载元素后是否应该开始下载视频数据。auto浏览器选择最佳行为,立即开始加载视频（如果浏览器支持）
        language: 'zh-CN',
        aspectRatio: '16:9', // 将播放器置于流畅模式，并在计算播放器的动态大小时使用该值。值应该代表一个比例 - 用冒号分隔的两个数字（例如"16:9"或"4:3"）
        fluid: true, // 当true时，Video.js player将拥有流体大小。换句话说，它将按比例缩放以适应其容器。
        sources: [{
          type: "video/mp4", // 类型
          src: "https://www.w3school.com.cn /i/movie.mp4"
        }],
        poster: './public/bg.png', // 封面地址
        notSupportedMessage: '此视频暂无法播放', // 允许覆盖Video.js无法播放媒体源时显示的默认信息。
        controlBar: {
          timeDivider: true, // 当前时间和持续时间的分隔符
          durationDisplay: true, // 显示持续时间
          remainingTimeDisplay: true, // 是否显示剩余时间功能
          fullscreenToggle: false // 是否显示全屏按钮
        }
      }
    }
  },
  methods: {
    download(){
      window.location.href = this.detail.videoPath
    }
  },
  mounted:function () {
    this.playerOptions.sources[0].src = this.detail.videoPath,
    console.log(this.playerOptions.sources[0].src)
  }
}
</script>

<style scoped>
#downBtn {
  height: 50px;
  width: 50px;
}
#videobox{
  margin-left: 7%;
  width: 75%;
  margin-bottom: 30px;
  box-shadow:3px 3px 5px 0px #787878;
  background-color: #ffffff

}
#title{
  padding-left: 20px;
  text-align: left;
  color: #4a83e7;
}
.demo{
  margin-bottom: 3%;
  display: inline-block;
  width: 600px;
  height: 338px;
  text-align: center;
  line-height: 100px;
  border: 1px solid transparent;
  border-radius: 4px;
  overflow: hidden;
  background: #ffffff;
  position: relative;
  box-shadow: 0 1px 1px;
  margin-right: 4px;
}
</style>