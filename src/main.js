import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import './plugins/elementui'
import Video from 'video.js'
import 'video.js/dist/video-js.css'

Vue.prototype.$video = Video

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
