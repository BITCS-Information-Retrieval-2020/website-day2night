import axios from "axios";

const HOST = "/host";

const base = {
  paper: "/api/papers",
};

const request = axios.create({
  baseURL: HOST,
  timeout: 5000,
  withCredentials: true,
});

// 实例，主动检索，通过关键词查找
// export function searchByKeywordApi(query) {
//   return request({
//     url: base.paper,
//     method: 'get',
//     params: query,
//     responseType: 'json'
//   })
// }
