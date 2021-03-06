import axios from "axios"

const HOST = "/host"
// const HOST = "http://10.63.185.189:8000"

const base = {
  // paper: "/api/papers",
  results: "/results/",
  hot: "/hot/",
  detail: "/detail/",
  suggest: "/suggest/home/",
}

const request = axios.create({
  baseURL: HOST,
  timeout: 5000,
  withCredentials: true,
})

// 实例，主动检索，通过关键词查找
// export function searchByKeywordApi(query) {
//   return request({
//     url: base.paper,
//     method: 'get',
//     params: query,
//     responseType: 'json'
//   })
// }

export function searchByKeywordApi(query) {
  return request({
    url: base.results,
    method: "get",
    params: query,
    responseType: "json",
  })
}

export function searchSuggestApi(query) {
  return request({
    url: base.suggest,
    method: "get",
    params: query,
    responseType: "json",
  })
}

export function hotApi(query) {
  return request({
    url: base.hot,
    method: "get",
    params: query,
    responseType: "json",
  })
}

export function detailApi(query) {
  return request({
    url: base.detail,
    method: "get",
    params: query,
    responseType: "json",
  })
}
