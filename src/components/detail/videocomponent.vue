<template>
  <div class='demo'>
    <video-player class="video-player vjs-custom-skin"
                  ref="videoPlayer"
                  :playsinline="true"
                  :options="playerOptions">
    </video-player>
  </div>
</template>

<script>
import { videoPlayer } from 'vue-video-player'
import 'video.js/dist/video-js.css'
export default {
  name: "videocomponent",
  components: {
    videoPlayer
  },
  data: function () {
    return {
      // playerOptions:{
      //   //播放速度
      //   playback:[0.5,1.0,1.25,1.5,2.0],
      //   //是否回放
      //   autoplay: false,
      //   //静音
      //   muted: false,
      //   //视频结束就重新开始
      //   loop: false,
      //   preload: 'auto',
      //   language:'zh-CN',
      //   aspectRatio: '16:9',
      //   fluid: true,
      //   source: [{
      //     type: "video/mp4",
      //     src: "https://vd3.bdstatic.com/mda-kket96s9pugq69t6/sc/mda-kket96s9pugq69t6.mp4?playlist=%5B%22hd%22%2C%22sc%22%5D&v_from_s=hba_haokan_4469&auth_key=1610781238-0-0-a9046559516d4c72013825817a9ab62a&bcevod_channel=searchbox_feed&pd=1&pt=3&abtest=8201_1-8656_1-8811_2"
      //   }],
      //   poster:"",
      //   notSupportedMessage: "此视频暂时无法播放",
      //   controlbar:{
      //     timeDivider:true,
      //     durationDisplay:true,
      //     remainingTimeDisplay:false,
      //     fullscreenToggle:true
      //   }
      // }
      // computed:{
      //   player(){
      //     return this.$refs.videoPlayer.player
      //   }
      // }
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
          type: ".video/mp4", // 类型
          src: 'https://www.w3school.com.cn/i/movie.mp4' // url地址
        }],
        poster: './public/bg.png', // 封面地址
        notSupportedMessage: '此视频暂无法播放，请稍后再试', // 允许覆盖Video.js无法播放媒体源时显示的默认信息。
        controlBar: {
          timeDivider: true, // 当前时间和持续时间的分隔符
          durationDisplay: true, // 显示持续时间
          remainingTimeDisplay: true, // 是否显示剩余时间功能
          fullscreenToggle: false // 是否显示全屏按钮
        }
      }
    }
  },

}
</script>

<style scoped>
/*.demo{*/
/*  display: inline-block;*/
/*  width: 600px;*/
/*  height: 338px;*/
/*  text-align: center;*/
/*  line-height: 100px;*/
/*  border: 1px solid transparent;*/
/*  border-radius: 4px;*/
/*  overflow: hidden;*/
/*  background: #ffffff;*/
/*  position: relative;*/
/*  box-shadow: 0 1px 1px;*/
/*  margin-right: 4px;*/
/*}*/
</style>