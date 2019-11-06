<template>
  <div class="basis-box">
    <el-container>
      <el-header>Header</el-header>
      <el-main>
        <el-container>
          <el-header>Header</el-header>
          <el-main style="width: 1200px;margin: 0 auto">
            <router-view></router-view>
          </el-main>
        </el-container>
      </el-main>
      <el-footer>
        <Fotter></Fotter>
      </el-footer>
    </el-container>
  </div>

</template>

<script>
  // @ is an alias to /src
import Fotter from '@/components/front-end/fotter.vue'

  export default {
    name: 'home',
    components: {
      Fotter,
    }
  }
</script>
<style>
  .basis-box{
    width: 100%;
    height: 100%;

  }
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }

  .el-main {
    color: #333;
    text-align: center;
    line-height: 160px;
    padding: 0!important;
  }
  .el-footer{
    width: 1200px;
    height: 270px!important;
    margin: 0 auto;

  }
</style>
