# irdisplay

## Project setup

```
npm install
```

### Compiles and hot-reloads for development

```
npm run serve
```

### Compiles and minifies for production

```
npm run build
```

### Lints and fixes files

```
npm run lint
```

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).

### 目录说明

views 存放页面。
components 存放各页面的组件，common 为公用组件，其余为对应 views 的组件。
plugins 使用到的插件，如 element-ui，插件的配置和使用放在插件文件夹下的 index.js 中
request 请求封装
router 页面路由
store vuex 状态管理
asset 存放静态资源，如图片

### 三个页面

Home.vue 主页
Result.vue 搜索结果页
Detail.vue 论文详情页
