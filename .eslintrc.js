module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: ["plugin:vue/essential", "eslint:recommended", "@vue/prettier"],
  parserOptions: {
    parser: "babel-eslint",
  },
  rules: {
    "no-console": process.env.NODE_ENV === "production" ? "warn" : "off",
    "no-debugger": process.env.NODE_ENV === "production" ? "warn" : "off",
    // 禁止使用 var，用let和const代替
    "no-var": "error",
    // 函数名括号前不需要有空格
    "space-before-function-paren": "off",
    // 代码块中避免多余留白
    "padded-blocks": "off",
    // 最多出现3个连续空行
    "no-multiple-empty-lines": [
      "error",
      {
        max: 3,
        maxBOF: 1,
      },
    ],
    curly: ["error", "all"], //必须使用 if(){} 中的{}
    indent: ["error", 2], //缩进风格2个空格
    semi: ["warn", "never"], //结尾不写分号
    "no-tabs": ["error"], // 禁用 tab
  },
}
