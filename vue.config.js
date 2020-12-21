const path = require("path");

function resolve(dir) {
  return path.join(__dirname, dir);
}

module.exports = {
  publicPath: "./",
  devServer: {
    proxy: {
      "/host": {
        // 此处的写法，目的是为了 将 /host 替换成 https://www.baidu.com/
        target: "",
        // 允许跨域
        changeOrigin: true,
        ws: true,
        pathRewrite: {
          "^/host": "",
        },
      },
    },
  },

  chainWebpack: (config) => {
    config.resolve.alias
      .set("@", resolve("src"))
      .set("src", resolve("src"))
      .set("common", resolve("src/components/common"))
      .set("components", resolve("src/components"))
      .set("request", resolve("src/request"))
      .set("store", resolve("src/store"));
  },
};
