<template>
  <div class="home">
    <el-container>
      <el-aside>
        <Aside></Aside>
      </el-aside>

      <el-container>
        <el-header>
          <Header></Header>
        </el-header>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>

    </el-container>
  </div>
</template>

<script>
  // @ is an alias to /src
  // import HelloWorld from '@/components/HelloWorld.vue'
  import Aside from '@/components/Aside/aside.vue'
  import Header from '@/components/Header/header.vue'

  export default {
    name: 'index',
    components: {
      // HelloWorld
      Aside,
      Header
    }
  }
</script>
<style>
  .home{
    width: 100%;
    height: 100%;
  }
  .el-aside {
    width: 100%;
    height: 100%;
    background-color: #ffffff;
    color: #333;
    text-align: center;
    /*line-height: 200px;*/
  }
  .el-container{
    width: 100%;
    height: 100%;
  }
  .el-main {
    background-color: #f7fafc;
    color: #333;
    text-align: center;
    /*line-height: 160px;*/
  }
  .el-header{
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    /*line-height: 60px;*/
  }
  .el-menu{
    border: none;
  }
  .el-menu-vertical-demo .el-submenu__title i{
    color: #67c1fd;
  }
  .el-menu-vertical-demo .el-submenu__title:hover{
    outline: 0 !important;
    color: #ffffff !important;
    background: -webkit-linear-gradient(left,#67c1fd,#71dcfd) !important;
  }
  .el-menu-vertical-demo .el-submenu__title:hover i{
    color: #ffffff!important;
  }
  .el-header{
    /*height: 80px!important;*/
    padding: 0!important;
    background-color: #ffffff;
  }
  .el-menu-demo .el-submenu__icon-arrow{
    display: none;
  }
  .er div{
    padding: 0!important;
  }
  .el-main{
    padding: 20px;
  }
  .el-menu-demo{
    border: none!important;
  }
  .el-card__body{
    padding-left: 40px!important;
  }
  .el-icon-bell{
    color: #67c1fd!important;
  }
  .el-icon-s-operation{
    color: #67c1fd!important;
  }
  .el-form-item__content{
        display: flex;
    }

  .hua .el-slider__bar{
    background: -webkit-linear-gradient(left,#46df8c,#46df8c);
  }
  .hua .el-slider__button{
    border: 2px solid #37c87d!important;
    box-shadow: 0 0 10px #37c87d;
  }
  .sf .el-slider__bar{
    background: -webkit-linear-gradient(left,#ff4145,#ff8190);
  }
  .sf .el-slider__button{
    border: 2px solid #ff4145!important;
    box-shadow: 0 0 10px #ff4145;
  }
  .cj .el-slider__bar{
    background: -webkit-linear-gradient(left,#68c0fc,#90ecfd);
  }
  .cj .el-slider__button{
    border: 2px solid #68c0fc!important;
    box-shadow: 0 0 10px #68c0fc;
  }
  .dj .el-slider__bar{
    background: -webkit-linear-gradient(left,#f7cd82,#fcdb7e);
  }
  .dj .el-slider__button{
    border: 2px solid #f7cd82!important;
    box-shadow: 0 0 10px #f7cd82;
  }
  .gj .el-slider__bar{
    background: -webkit-linear-gradient(left,#cc78e7,#fca3f9);
  }
  .gj .el-slider__button{
    border: 2px solid #cc78e7!important;
    box-shadow: 0 0 10px #cc78e7;
  }
  .el-upload--picture-card{
    width: 80px!important;
    height: 80px!important;
    background-color: #d5d5d5;
    margin-top: 20px;
  }
  .el-upload--picture-card i{
    color: white;
    position: absolute;
    left: 72px;
    top: 64px;
  }
</style>
