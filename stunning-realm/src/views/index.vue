<template>
  <el-backtop :right="100" :bottom="100" />
  <div class="container">
    <div class="header">
      <div class="header-logo">
        <img src="../assets/logo.svg" alt="" class="w-32 h-32" />
      </div>
      <div class="header-nav">
        <el-menu
          :default-active="selectedMenu"
          mode="horizontal"
          background-color="#FFFFFF"
          text-color="#666"
          active-text-color="#d60b0a"
          @select="handleSelect"
        >
          <el-menu-item index="1">首页</el-menu-item>
          <el-sub-menu index="2">
            <template #title>排名</template>
            <el-menu-item index="2-1">中国大学排名</el-menu-item>
            <el-menu-item index="2-2">中国最好学科排名</el-menu-item>
            <el-menu-item index="2-3">中国大学专业排名</el-menu-item>
            <el-menu-item index="2-4">世界大学排名</el-menu-item>
          </el-sub-menu>
          <el-menu-item index="3">院校</el-menu-item>
          <el-menu-item index="4">报告</el-menu-item>
          <el-menu-item index="5">资讯</el-menu-item>
        </el-menu>
      </div>
      <div class="header-english">
        <div class="lang-container">English</div>
      </div>
      <div class="right-container">
        <div class="header-user">
          <span>登录/注册</span>
        </div>
      </div>
    </div>
    <div class="main">
      <div class="top-bar">
        <div class="textsxpansion">
          <div class="content title"></div>
          <div class="content desc"></div>
        </div>
        <el-carousel :interval="4000" type="card" height="350px" width="600px">
          <el-carousel-item v-for="(image, index) in carouselImages" :key="index">
            <el-image fit="contain" :src="image" />
          </el-carousel-item>
        </el-carousel>
      </div>
      <div class="main-content">
        <div class="content-box">
          <div class="table-title">
            <div class="decoration"></div>
            <div class="title-name">
              中国大学排名（主榜）
              <span class="title-desc">共 {{ totalCount }} 所学校</span>
            </div>
            <div class="search">
              <el-input
                clearable
                placeholder="请输入学校名称"
                v-model.trim="searchCollege"
                width="280px"
                @keyup.enter="searchCollegeByName"
              ></el-input>
            </div>
          </div>
          <div class="table-box">
            <el-table :data="tableData" style="width: 100%" height="1850">
              <el-table-column prop="rank" label="排名" width="60" />
              <el-table-column prop="name" label="学校名称" width="300">
                <template #default="scope">
                  <div class="univname-container">
                    <div class="logo">
                      <el-avatar :size="60" src=""></el-avatar>
                    </div>
                    <div class="univname">
                      <div class="cn-name">{{ scope.row.cn_name }}</div>
                      <div class="en-name">{{ scope.row.en_name }}</div>
                      <p class="tags">{{ scope.row.tags }}</p>
                    </div>
                  </div>
                </template>
              </el-table-column>
              <el-table-column prop="province" :ref="selectedProvince" width="100">
                <template #header>
                  <el-select
                    v-model="selectedProvince"
                    placeholder="选择省份"
                    @change="filterByProvince"
                  >
                    <el-option
                      v-for="(label, value) in provinceOptions"
                      :key="value"
                      :label="label"
                      :value="label"
                    ></el-option>
                  </el-select>
                </template>
              </el-table-column>
              <el-table-column prop="type" :label="selectedType" width="100">
                <template #header>
                  <el-select v-model="selectedType" placeholder="选择类型" @change="filterByType">
                    <el-option
                      v-for="(label, value) in typeOptions"
                      :key="value"
                      :label="label"
                      :value="label"
                    ></el-option>
                  </el-select>
                </template>
              </el-table-column>
              <el-table-column prop="score" label="总分" width="100" />
              <el-table-column prop="level" label="办学层次" width="140" />
            </el-table>
          </div>
          <div class="pagination">
            <el-pagination
              background
              :current-page="paginationData.current"
              :page-size="paginationData.limit"
              :page-count="page_count"
              :total="totalCount"
              layout="jumper, prev, pager, next, total"
              @current-change="getPaginationData"
            />
          </div>
        </div>
        <div class="content-side">
          <div class="rank-title">
            <div class="decoration"></div>
            <span class="side-title">中国大学排名</span>
          </div>
          <div class="rank-menu">
            <el-menu default-active="/" class="el-menu" :router="false">
              <el-menu-item index="/"> 中国大学排行 (主榜) </el-menu-item>
              <el-menu-item index="/medicine"> 中国医药类大学排名 </el-menu-item>
              <el-menu-item index="/economic"> 中国财经类大学排名 </el-menu-item>
              <el-menu-item index="/language"> 中国语言类大学排名 </el-menu-item>
              <el-menu-item index="/policy"> 中国政法类大学排名 </el-menu-item>
              <el-menu-item index="/ethics"> 中国民族类大学排名 </el-menu-item>
            </el-menu>
          </div>
        </div>
      </div>
    </div>
    <footer class="relative bg-blueGray-200 pt-8 pb-6">
      <div class="container mx-auto px-4">
        <div class="flex flex-wrap text-left lg:text-left">
          <div class="w-full lg:w-6/12 px-4">
            <h4 class="text-3xl fonat-semibold text-blueGray-700">欢迎与我们保持联系！</h4>
            <h5 class="text-lg mt-0 mb-2 text-blueGray-600">
              一起学习新知识、分享经验、共同进步！
            </h5>
          </div>
          <div class="w-full lg:w-6/12 px-4">
            <div class="flex flex-wrap items-top mb-6">
              <div class="w-full lg:w-4/12 px-4 ml-auto">
                <span class="block uppercase text-blueGray-500 text-sm font-semibold mb-2"
                  >Useful Links</span
                >
                <ul class="list-unstyled">
                  <li>
                    <a
                      class="text-blueGray-600 hover:text-blueGray-800 font-semibold block pb-2 text-sm"
                      href=""
                      >About Us</a
                    >
                  </li>
                  <li>
                    <a
                      class="text-blueGray-600 hover:text-blueGray-800 font-semibold block pb-2 text-sm"
                      href=""
                      >Blog</a
                    >
                  </li>
                  <li>
                    <a
                      class="text-blueGray-600 hover:text-blueGray-800 font-semibold block pb-2 text-sm"
                      href=""
                      >Github</a
                    >
                  </li>
                  <li>
                    <a
                      class="text-blueGray-600 hover:text-blueGray-800 font-semibold block pb-2 text-sm"
                      href=""
                      >Free Products</a
                    >
                  </li>
                </ul>
              </div>
              <div class="w-full lg:w-4/12 px-4">
                <span class="block uppercase text-blueGray-500 text-sm font-semibold mb-2"
                  >Other Resources</span
                >
                <ul class="list-unstyled">
                  <li>
                    <a
                      class="text-blueGray-600 hover:text-blueGray-800 font-semibold block pb-2 text-sm"
                      href=""
                      >MIT License</a
                    >
                  </li>
                  <li>
                    <a
                      class="text-blueGray-600 hover:text-blueGray-800 font-semibold block pb-2 text-sm"
                      href=""
                      >Terms &amp; Conditions</a
                    >
                  </li>
                  <li>
                    <a
                      class="text-blueGray-600 hover:text-blueGray-800 font-semibold block pb-2 text-sm"
                      href=""
                      >Privacy Policy</a
                    >
                  </li>
                  <li>
                    <a
                      class="text-blueGray-600 hover:text-blueGray-800 font-semibold block pb-2 text-sm"
                      href=""
                      >Contact Us</a
                    >
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
        <hr class="my-6 border-blueGray-300" />
        <div class="flex flex-wrap items-center md:justify-between justify-center">
          <div class="w-full md:w-4/12 px-4 mx-auto text-center">
            <div class="text-sm text-blueGray-500 font-semibold py-1">
              Copyright © <span id="get-current-year">2024</span>
              <a
                href="https://github.com/294916437/stunning-realm"
                class="text-blueGray-500 hover:text-gray-800"
                target="_blank"
              >
                Stunning Realm by
              </a>
              <a
                href="https://github.com/294916437"
                class="text-blueGray-500 hover:text-blueGray-800"
                >Asams Morgan</a
              >.
            </div>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, reactive } from 'vue'
import { useCollegeStore } from '@/store/college'
import { storeToRefs } from 'pinia'
const store = useCollegeStore()
const { colleges } = storeToRefs(store)
const images = import.meta.glob('../assets/carousel_*.jpg', { eager: true })
const carouselImages = ref(Object.values(images).map((mod) => mod.default))
const handleSelect = () => {}
const selectedMenu = ref('2-1')
const paginationData = reactive({
  current: 1,
  limit: 20
})
const provinceOptions = [
  '全部',
  '北京',
  '天津',
  '河北',
  '山西',
  '内蒙古',
  '辽宁',
  '吉林',
  '黑龙江',
  '上海',
  '江苏',
  '浙江',
  '安徽',
  '福建',
  '江西',
  '山东',
  '河南',
  '湖北',
  '湖南',
  '广东',
  '广西',
  '海南',
  '重庆',
  '四川',
  '贵州',
  '云南',
  '西藏',
  '陕西',
  '甘肃',
  '青海',
  '宁夏',
  '新疆'
]
const typeOptions = {
  0: '全部',
  1: '综合',
  2: '理工',
  3: '师范',
  4: '农业',
  5: '林业'
}
const searchCollege = ref()
const selectedProvince = ref('全部')
const selectedType = ref('全部')
const tableData = ref([])
const totalCount = computed(() => colleges.value.length)
const page_count = computed(() => Math.ceil(totalCount.value / paginationData.limit))
const getCollegeInfo = async () => {
  await store.getCollegeInfo()
}

// 按名称搜索大学
const searchCollegeByName = () => {
  let results = colleges.value.filter(
    (college) =>
      college.cn_name.includes(searchCollege.value) || college.en_name.includes(searchCollege.value)
  )
  tableData.value = results
}

//分页查询逻辑
const pageQuery = () => {
  let begin = paginationData.current * paginationData.limit - paginationData.limit
  tableData.value = colleges.value.slice(begin, begin + paginationData.limit)
}
function getPaginationData(page = 1) {
  paginationData.current = page
  pageQuery()
}
// 筛选省份的方法
const filterByProvince = () => {
  if (selectedProvince.value == '全部') {
    getPaginationData()
  } else {
    tableData.value = colleges.value.filter(
      (college) => college.province === selectedProvince.value
    )
  }
}
// 筛选类型的方法
const filterByType = () => {
  if (selectedType.value == '全部') {
    getPaginationData()
  } else {
    tableData.value = colleges.value.filter((college) => college.type === selectedType.value)
  }
}
onMounted(async () => {
  await getCollegeInfo()
  getPaginationData()
})
</script>

<style lang="css" scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  max-width: 100vw;
  width: 100%;
  margin: 0 auto;
}
.header {
  z-index: 66;
  position: fixed;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 64px;
  width: 100%;
  background-color: #fff;
  padding-left: 200px;
  padding-right: 200px;
  box-shadow: 0 2px 2px rgba(0, 0, 0, 0.1);
}

.main {
  margin: 64px auto;
}
.top-bar {
  width: 100%;
  background-image: url('../assets/top_background.png');
}
:deep(.el-carousel__container) {
  width: 100vw;
}
.el-carousel__item h3 {
  color: #475669;
  opacity: 0.8;
  line-height: 350px;
  margin: 0;
  text-align: center;
}
.main {
  background-color: #f7f9fa;
}
.main-content {
  display: flex;
  flex-direction: row;
  justify-content: center;
  width: 100vw;
  padding-top: 20px;
  gap: 40px;
}
.content-box {
  padding: 16px;
  background-color: #fff;
  width: 832px;
}
.content-side {
  height: 280px;
  width: 280px;
  background-color: #fff;
}
.table-title {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  margin-bottom: 16px;
}
.title-name {
  font-size: 1.4rem;
  color: #383638;
}
.title-desc {
  font-size: 1rem;
  color: #aeaeae;
  margin-right: 280px;
}
.univname-container {
  display: flex;
  justify-content: flex-start;
  gap: 16px;
}
.univname {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.cn-name {
  color: #383638;
  font-size: 16px;
}
.en-name {
  color: #8e8c8e;
}
.tags {
  color: #8d8b8d;
}
.decoration {
  width: 4px;
  height: 18px;
  background-color: #e5002d;
  border-radius: 0 2px 2px 0;
}
.side-title {
  margin-left: 24px;
}
.rank-title {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  height: 56px;
  padding: 12px;
  font-size: 1.2rem;
  color: #383638;
  padding-left: 0;
}
:deep(.el-pagination) {
  margin: 6px auto;
  margin-left: 120px;
}
.footer {
  width: 100%;
  margin: 0 auto;
}
</style>
