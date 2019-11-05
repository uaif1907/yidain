<template>
  <div class="hello">

    <el-col :span="24">
      <div class="box">
        <i class="logo"></i>
        <div class="size">
          <span>一点生活</span>
          <span>A LITTLE LIFE</span>
        </div>
      </div>

      <el-menu
              class="el-menu-vertical-demo"
              @open="handleOpen"
              @close="handleClose"
              background-color="#ffffff"
              text-color="#333"
              active-text-color="#ffffff"
      >
        <router-link tag="div" :to="{name:'home'}">
          <el-menu-item index="1">
            <i class="el-icon-s-home"></i>
            <span slot="title">首页信息</span>
          </el-menu-item>
        </router-link>


        <el-submenu index="2">
          <template slot="title">
            <router-link tag="div" :to="{name:'order'}">
              <i class="el-icon-s-order"></i>
              <span>订单管理</span>
            </router-link>
          </template>
          <el-menu-item-group>
            <router-link tag="div" :to="{name:'paid'}">
              <el-menu-item index="2-1">
                <i class="el-icon-success"></i>
                <span>有效订单</span>
              </el-menu-item>
            </router-link>
            <router-link tag="div" :to="{name:'unpaid'}">
              <el-menu-item index="2-2">
                <i class="el-icon-error"></i>
                <span>无效订单</span>
              </el-menu-item>
            </router-link>
          </el-menu-item-group>
        </el-submenu>

        <el-submenu index="3">
          <template slot="title">
            <router-link tag="div" :to="{name:'cargo'}">
              <i class="el-icon-s-finance"></i>
              <span>货物管理</span>
            </router-link>
          </template>

          <el-menu-item-group>
            <router-link tag="div" :to="{name:'ground'}">
              <el-menu-item index="3-1">
                <i class="el-icon-success"></i>
                <span>已上架</span>
              </el-menu-item>
            </router-link>
            <router-link tag="div" :to="{name:'notground'}">
              <el-menu-item index="3-2">
                <i class="el-icon-error"></i>
                <span>未上架</span>
              </el-menu-item>
            </router-link>
          </el-menu-item-group>
        </el-submenu>
        <router-link tag="div" :to="{name:'user'}">
          <el-menu-item index="4">
            <i class="el-icon-s-custom"></i>
            <span slot="title">用户管理</span>
          </el-menu-item>
        </router-link>
        <router-link tag="div" :to="{name:'datam'}">
          <el-menu-item index="5">
            <i class="el-icon-pie-chart"></i>
            <span slot="title">数据管理</span>
          </el-menu-item>
        </router-link>

      </el-menu>
    </el-col>

  </div>
</template>

<script>
  export default {
    name: 'Aside',
    props: {
      // msg: String
    },
    methods: {
      handleOpen() {
      },
      handleClose() {
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .box{
    width: 300px;
    height: 105px;
    padding-bottom: 25px;
    box-sizing: border-box;
    /*line-height: 80px;*/
  }
  .el-menu-item:hover{
    outline: 0 !important;
    color: #ffffff !important;
    background: -webkit-linear-gradient(left,#67c1fd,#71dcfd) !important;
  }
  .el-menu-item:hover i{
    color: #ffffff!important;
  }
  .el-menu-item i{
    color: #67c1fd;
  }
  .el-menu-item.is-active{
    color: #fff !important;
    background: -webkit-linear-gradient(left,#67c1fd,#71dcfd) !important;
  }
  .el-menu-item.is-active i{
    color: white!important;
  }
  .box{
    display: flex;
    justify-content: center;
  }
  .logo{
    width: 49px;
    height: 49px;
    background: url("../../assets/logo.png") no-repeat;
    background-size: contain;
    margin: 12px 27px 20px 58px;
  }
  .size{
    height: 32px;
    display: flex;
    flex-direction: column;
    align-content: center;
    border-left: 2px solid #7f7f7f;
    box-sizing: border-box;
    font-size: 12px;
    margin-top: 20px;
  }
  .size span{
    width: 94px;
    height: 18px;
    line-height: 18px;
    text-align: center;
  }
  .size span:first-child{
    color: #191919;
    font-weight: 600;
  }
  .size span:last-child{
    color: #7f7f7f;
  }

</style>
