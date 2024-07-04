// ts声明识别vue文件
declare module '*.vue' {
  import { DefineComponent } from 'vue'
  const component: DefineComponent<{}, {}, any>
  export default component
}
// ts声明识别js文件
declare module '@/utils/request' {
  export function request(url: string, params: object, type: string): Promise<any>
}
