import { defineStore } from 'pinia'
import { reactive } from 'vue'
import { ElMessage } from 'element-plus'
import { request } from '@/utils/request'
interface college {
  id: number
  rank: number
  cn_name: string
  en_name: string
  tags: string
  province: string
  score: number
  logo_url: string
  level: string
}
export const useCollegeStore = defineStore('colleges', () => {
  const colleges = reactive<college[]>([])
  const getCollegeInfo = async () => {
    const result = await request('/college/', {}, 'GET')
    if (result.code == 200) {
      ElMessage({
        message: '获取数据成功',
        type: 'success',
        center: true
      })
      Object.assign(colleges, result.data)
    } else {
      ElMessage({
        message: '获取数据失败',
        type: 'error',
        center: true
      })
    }
  }
  return { colleges, getCollegeInfo }
})
