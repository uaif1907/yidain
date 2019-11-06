<template>
  <div class="details" style="width:1200px;margin:auto;height:auto;">
    <el-breadcrumb separator="/" class="bread">
      <div class="yuandian1"></div>
      <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item><a href="/">座椅</a></el-breadcrumb-item>
      <el-breadcrumb-item>北欧旅程</el-breadcrumb-item>
    </el-breadcrumb>
    <div class="showbox">
      <div class="showimg">
        <img src="../../assets/details-img/chair1.png" alt="231" style="height:600px;">
      </div>
      <div class="showtext">
        <div><img src="../../assets/details-img/text1.png" alt=""></div>
        <div><img src="../../assets/details-img/text2.png" alt=""></div>
        <div class="yellowline"></div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src


export default {
  name: 'details',
  components: {

  }
}
</script>
<style >
  .bread{
    padding: 10px;
    font-size:15px;
  }
  .showbox{
    width: 100%;
    height:730px;
    display: flex;
  }
  .showimg{
    width:600px;
    height:100%;
  }
  .showtext{
    width:600px;
    height:100%;
  }
  .yuandian1{
    float:left;
    width:10px;
    height:10px;
    background-color: #5ed5e0;
    border-radius: 50%;
    margin: 2px 20px;
  }
  .yellowline{
    width:30px;
    height:8px;
    border-radius: 5px;
    background-color: #ffc04b;
  }
</style>