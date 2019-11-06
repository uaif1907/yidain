<template>
  <div class="list-box">
<!--    轮播-->
    <el-carousel class="banner-box">
      <el-carousel-item v-for="item in 4" :key="item">
      </el-carousel-item>
    </el-carousel>
<!--查询-->
    <el-row :span="24" style="background-color: lightgoldenrodyellow;height: 456px;">
      <el-row :span="24" style="background-color: lightblue;height: 124px;">
2
      </el-row>
      <el-row :span="24" style="background-color: lightcoral;height: 332px"></el-row>
    </el-row>
<!--列表-->
    <el-row :span="24" style="height: 456px;display: flex">
      <el-col :span="12" style="background-color: #2c3e50"></el-col>
      <el-col :span="6" style="background-color: #42b983"></el-col>
      <el-col :span="6" style="background-color: pink"></el-col>
    </el-row>
  </div>
</template>

<script>
  // @ is an alias to /src

  export default {
    name: 'lists',
    components: {

    }
  }
</script>

<style scoped>
  .list-box{
    width: 1200px;
  }
  .el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    margin: 0;
  }
  .banner-box{
      margin-top: 10px;
  }
  .el-carousel__item:nth-child(n) {
    background: url("../../../assets/list/lb1.png") no-repeat;
    background-size: 100% 100%;
  }
  .el-carousel__item:nth-child(2n) {
    background: url("../../../assets/list/lb2.png") no-repeat;
    background-size: cover;
  }
  .el-carousel__item:nth-child(3) {
    background: url("../../../assets/list/lb3.png") no-repeat;
    background-size: cover;
  }
  .el-carousel__item:nth-child(4){
    background: url("../../../assets/list/lb4.png") no-repeat;
    background-size: cover;
  }
  .banner-box{
    height: 500px!important;
  }
  .el-carousel__container{
    height: 500px!important;
  }
</style>
