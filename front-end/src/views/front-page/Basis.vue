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
      <el-footer>Footer</el-footer>
    </el-container>
  </div>

</template>

<script>
  // @ is an alias to /src


  export default {
    name: 'home',
    components: {

    }
  }
</script>
<style>
  .basis-box{
    width: 100%;
    height: 100%;

  }
  .el-header, .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }

  .el-main {
    color: #333;
    text-align: center;

    padding: 0!important;
  }
<<<<<<< HEAD
=======

  .el-footer{
    width: 1200px;
    height: 270px!important;
    margin: 0 auto;
    padding: 0!important;
  }

  .headers-box{
    height: 80px!important;

  }
  .el-carousel__container{
    height: 500px!important;
  }
  .el-input__inner{
    border-radius: 20px;
  }
  .el-radio-button__inner{
    border-radius: 20px!important;
    width: 104px;
    border: 1px solid #a9a9a9!important;
  }
  .el-radio-button__orig-radio:checked+.el-radio-button__inner{
    background-color: #5ed5e0!important;
    border: 1px solid #5ed5e0!important;
    -webkit-box-shadow: -1px 0 0 0 #5ed5e0!important;
  }
  .tie-box .el-form-item__label{
    width: 90px!important;
  }
  .input-box .el-input__inner {
    border: 1px solid #a9a9a9!important;
  }
>>>>>>> b8d1b6bf3c439ca9e9a5a7ad69cf3d83eb453e0e
</style>
