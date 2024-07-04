import axios from 'axios'
import { ElMessage } from 'element-plus' // 引入el 提示框

// 创建axios实例
const service = axios.create({
  baseURL: import.meta.env.VITE_API_POST,
  timeout: 5000, // 请求超时时间
  withCredentials: true //携带HttpOnly cookie
})

//http request 拦截器
service.interceptors.request.use(
  (config) => {
    // 配置请求头
    config.headers = {
      'Content-Type': 'application/json;charset=UTF-8',
      'X-Requested-With': 'XMLHttpRequest'
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

//http response 拦截器
service.interceptors.response.use(
  (response) => {
    return response.data
  },
  (error) => {
    if (error.response) {
      return Promise.resolve(error.response.data)
    } else {
      ElMessage.error('网络错误或请求未发出')
      return Promise.reject(error)
    }
  }
)

// 封装 GET POST PUT请求并导出
export function request(url = '', params = {}, type = '') {
  return new Promise((resolve, reject) => {
    let promise
    switch (type) {
      case 'GET':
        promise = service.get(url)
        break
      case 'POST':
        promise = service.post(url, params)
        break
      case 'PUT':
        promise = service.put(url, params)
        break
      default:
    }
    //处理返回
    promise
      .then((res) => {
        resolve(res)
      })
      .catch((err) => {
        reject(err)
      })
  })
}
