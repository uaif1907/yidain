<template>
  <div class="person-box">
    <!-- 这里是头部面包屑 -->
    <div class="crumbs">
      <div class="index-person">
        <div class="yuan"></div>
        <el-breadcrumb separator="/" class="person_crumbs">
          <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
          <el-breadcrumb-item>个人中心</el-breadcrumb-item>
        </el-breadcrumb>
      </div>
    </div>
    <!-- 这里是主体哦 -->
    <div class="person-main">
      <!--左侧导航-->
      <div class="person_left">
        <!--logo盒子-->
        <div class="left_logobox">
          <div class="left_logo"></div>
          <div class="logo_text">青 花 瓷 的 秘 密</div>
          <div class="logo_vip"></div>
        </div>
        <!--内容盒子-->
        <div class="left_conboxs">
          <!--单独小块盒子-->
          <div class="conbox">
            <!--盒子头-->
            <div class="conbox_title">
              <div class="title_logo"><img src="../../assets/person_img/图层65.png" alt=""></div>
              <div class="title_g"></div>
              <div class="title_text">个 · 人 · 中 · 心</div>
              <div class="title_english">Personal    information.</div>
            </div>
            <!--盒子内容-->
            <div class="conbox_con">
              <div class="conbox_body">
                <div class="con_logobox"><img src="../../assets/person_img/图层66.png" alt=""></div>
              <span>我的资料 / My profile</span>
              </div>
              <div class="conbox_body">
                <div class="con_logobox"><img src="../../assets/person_img/图层70.png" alt=""></div>
              <span>收货地址管理 / Receiving address</span>
              </div>
              <div class="conbox_body">
                <div class="con_logobox"><img src="../../assets/person_img/图层67.png" alt=""></div>
              <span>账户安全 / Account security</span>
              </div>
            </div>
          </div>
          <div class="conbox">
            <!--盒子头-->
            <div class="conbox_title">
              <div class="title_logo" style="position: absolute;left: 35px"><img src="../../assets/person_img/图层69.png" alt=""></div>
              <div class="title_g"></div>
              <div class="title_text">我 · 的 · 订 · 单</div>
              <div class="title_english">My order.</div>
            </div>
            <!--盒子内容-->
            <div class="conbox_con">
              <div class="conbox_body">
                <div class="con_logobox"><img src="../../assets/person_img/图层71.png" alt=""></div>
              <span>我的订单 / My order</span>
              </div>
              <div class="conbox_body">
                <div class="con_logobox"><img src="../../assets/person_img/图层72.png" alt=""></div>
              <span>退换货管理 / Return and Exchange</span>
              </div>
              <div class="conbox_body">
                <div class="con_logobox"><img src="../../assets/person_img/图层73.png" alt=""></div>
              <span>我的优惠券 / My coupon</span>
              </div>
            </div>
          </div>
          <div class="conbox">
            <!--盒子头-->
            <div class="conbox_title">
              <div class="title_logo" style="position: absolute;left: 42px;top: 21px"><img src="../../assets/person_img/图层75拷贝.png" alt=""></div>
              <div class="title_logo" style="position: absolute;left: 50px;top: 10px"><img src="../../assets/person_img/图层75.png" alt=""></div>
              <div class="title_g"></div>
              <div class="title_text">服 · 务 · 中 · 心</div>
              <div class="title_english">Service Center.</div>
            </div>
            <!--盒子内容-->
            <div class="conbox_con">
              <div class="conbox_body">
                <div class="con_logobox"><img src="../../assets/person_img/图层76.png" alt=""></div>
              <span>物流管理 / Logistics Management</span>
              </div>
              <div class="conbox_body">
                <div class="con_logobox"><img src="../../assets/person_img/图层77.png" alt=""></div>
              <span>售后管理 / After-sales</span>
              </div>
              <div class="conbox_body">
                <div class="con_logobox"><img src="../../assets/person_img/图层78.png" alt=""></div>
              <span>联系客服 / Contact Customer</span>
              </div>
              <div class="conbox_body">
                <div class="con_logobox"><img src="../../assets/person_img/图层79.png" alt=""></div>
              <span>我的维权 / My rights</span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!--右侧内容区 信息栏-->
      <div class="person_right">
        <div class="right_tx"></div>
        <div class="tx_text">青 花 瓷 的 秘 密</div>
        <div class="tx_text2">我们不相信会有完美无缺的家，要相信自己可以~~<i class="el-icon-edit" style="margin-left: 5px"></i></div>
        <div class="tx_talk" style="position: absolute;right: 150px;top:30px"><img src="../../assets/person_img/图层81.png" alt=""></div>
        <div class="tx_shop" style="position: absolute;right: 80px;top:30px"><img src="../../assets/person_img/购物袋拷贝.png" alt=""></div>
      </div>
    </div>
  </div>
</template>

<script>
  // @ is an alias to /src


  export default {
    name: 'person-box',
    components: {

    }
  }
</script>
<style scoped>
  .person-box{
    width: 1200px;
    height: 100%;
    /*background-color: #37c87d;*/
  }
  .crumbs{
    width: 100%;
    height: 175px;
    /*background-color: #2c3e50;*/
    padding-top: 40px;
    padding-left: 20px;
    box-sizing: border-box;
  }
  .index-person{
    width: 200px;
    height: 50px;
    /*background-color: lightgoldenrodyellow;*/
  }
  .index-person .yuan{
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background-color: #4cc0cb;
    float: left;
    margin-top: 21px;
  }
  .person_crumbs{
    float: left;
    margin-top: 18px;
    margin-left: 10px;
  }
  .person-main{
    width: 1200px;
  }
  .person_left{
    width: 250px;
    background-color: #ffffff;
    float: left;
    border: 2px solid #e5e5e5;
    box-sizing: border-box;
  }
  .left_logobox{
    width: 100%;
    height: 130px;
    /*background-color: #2c3e50;*/
    position: relative;
  }
  .left_logo{
    width: 60px;
    height: 100px;
    background: url("../../assets/person_img/图层62.png");
    background-size: cover;
    position: absolute;
    top: -50px;
    left: 88px;
  }
  .logo_text{
    width: 100%;
    font-weight: 600;
    font-size: 16px;
    position: absolute;
    top: 50px;
  }
  .logo_vip{
    width: 25px;
    height: 20px;
    background: url("../../assets/person_img/图层64.png");
    background-size: cover;
    position: absolute;
    top: 80px;
    left: 105px;
  }
  .left_conboxs{
    width: 100%;
  }
  .conbox{
    width: 100%;
  }
  .conbox_title{
    width: 100%;
    height: 60px;
    background-color: #f3f3f3;
    position: relative;
  }
  .conbox_con{
    width: 100%;
    padding: 20px 10px;
    box-sizing: border-box;
  }
  .title_logo{
    position: absolute;
    left: 40px;
    top: 12px;
  }
  /*.title_logo img{*/
  /*  width: 100%;*/
  /*  height: 100%;*/
  /*}*/
  .title_g{
    width: 2px;
    height: 20px;
    background-color: #c2c2c2;
    position: absolute;
    left: 70px;
    top: 17px;
  }
  .title_text{
    font-size: 14px;
    font-weight: 600;
    position: absolute;
    top: 10px;
    left: 80px;
  }
  .title_english{
    font-weight: 400;
    font-size: 12px;
    color: #989898;
    position: absolute;
    top: 30px;
    left: 80px;
  }
  .conbox_body{
    width: 100%;
    height: 20px;
    margin: 15px 0;
  }
  .con_logobox{
    width: 15px;
    height: 15px;
    float: left;
    margin-top: 2px;
    margin-left: 5px;
  }
  .conbox_body img{
    width: 100%;
    height: 100%;
  }
  .conbox_body span{
    font-size: 12px;
    color: #a6a6a6;
    font-weight: 600;
    float: left;
    margin-left: 10px;
    margin-top: 2px;
  }
  .person_right{
    width: 900px;
    height: 190px;
    background-color: #ffffff;
    float: right;
    border: 2px solid #e5e5e5;
    position: relative;
  }
  .right_tx{
    width: 50px;
    height: 48px;
    border-radius: 50%;
    /*background-color: #37c87d;*/
    border: 2px solid #f3f3f3;
    background: url("../../assets/person_img/图层62.png");
    background-size: cover;
    position: absolute;
    top: 20px;
    left: 30px;
    box-sizing: border-box;
  }
  .tx_text{
    font-weight: 600;
    font-size: 16px;
    position: absolute;
    left: 100px;
    top: 20px;
  }
  .tx_text2{
    color: #626262;
    font-weight: 600;
    font-size: 12px;
    position: absolute;
    left: 100px;
    top: 46px;
  }
</style>