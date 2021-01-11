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

- views 存放页面。
- components 存放各页面的组件，common 为公用组件，其余为对应 views 的组件。
- plugins 使用到的插件，如 element-ui，插件的配置和使用放在插件文件夹下的 index.js 中
- request 请求封装
- router 页面路由
- store vuex 状态管理
- asset 存放静态资源，如图片

### 三个页面

这三个页面都在 views 里面
Home.vue 主页
Result.vue 搜索结果页
Detail.vue 论文详情页

### 参考资料

- element-ui：https://element.eleme.cn/#/zh-CN/component/installation

### 一些开发建议

1. 开发流程：

   - 在 views 中对应 vue 文件中写页面
   - （碰到了需要做网络请求）在 request>index.js 中写发送请求的代码，在自己的.vue 页面文件中引入 request/index.js
   - （碰到了页面某一部分可以独立抽出来，例如页面可以分为几大块，每一块之间可能没有多大关联）在 components>页面>下创建组件 vue 文件，在自己页面引入这个 vue 文件

2. 推荐 vscode 插件
   如果你使用 vscode 进行 vue 开发，推荐你安装以下插件：

- vetur vue 的开发插件
- Auto Close Tag 可以自动补全 html</>标签
- Auto Rename Tag 可以自动更改 html 标签
- Bracket Pair Colorizer2 可以让括号变彩色！！！好看！！
- Npm Intellisense 自动补全 import moudle
- Power Mode 没什么用，能让代码爆炸，美观插件
