<template>
  <div class="basis-box">
    <el-container>
      <el-header style="background-color: #f3f3f3;">
        <Header></Header>
      </el-header>
      <el-main>
        <el-container>
          <el-header class="headers-box">
            <Nav></Nav>
          </el-header>
          <el-main style="margin: 0 auto">
            <router-view></router-view>
          </el-main>
        </el-container>
      </el-main>
      <el-footer>
        <Footer></Footer>
      </el-footer>
    </el-container>
  </div>

</template>

<script>
  // @ is an alias to /src
  import Header from '@/components/front-end/header.vue'
  import Nav from '@/components/front-end/nav.vue'
  import Footer from '@/components/front-end/footer.vue'
  export default {
    name: 'home',
    components: {
      Header,
      Nav,
      Footer
    }
  }
</script>
<style>
  .basis-box{
    width: 100%;
    height: 100%;

  }
  .el-header{
    color: #333;
    text-align: center;
    line-height: 60px;
  }

  .el-main {
    color: #333;
    text-align: center;
    padding: 0!important;
  }
  .headers-box{
    height: 80px!important;
  }
  .el-carousel__container{
    height: 500px!important;
  }
</style>
