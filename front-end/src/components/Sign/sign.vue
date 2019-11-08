<template>
  <div class="he">
    <el-form ref="form"  style="background-color: #ffffff;width: 360px;overflow: hidden;" size="medium">
      <div class="Title" style="font-weight:bold">登陆</div>
      <div class="Title1">
        <div class="box" style="margin-left: 80px">
          <div class="box-one"></div>
          <div class="box-two"></div>
        </div>
        <p style="font-size: 12px;color: #ccc">WELCOME</p>
        <div class="box" style="margin-right: 80px">
          <div class="box-two"></div>
          <div class="box-one"></div>
        </div>
      </div>
  <el-form-item >
    <div class="Boxone">
      <el-input v-model="form.name" style="width: 280px;border-radius:0;font-size: medium" prefix-icon="el-icon-mobile-phone"></el-input>
      <p style="background: white;padding: 0 10px">手机号/账号/邮箱</p>
    </div>
  </el-form-item>
   <el-form-item style="margin-bottom: 15px">
    <div class="Boxtwo">
       <el-input v-model="form.name" style="width: 280px;border-radius:0;font-size: medium" prefix-icon="el-icon-lock"></el-input>
      <p style="background: white;padding: 0 10px">密码</p>
    </div>
   </el-form-item>
  <el-form-item >
    <div class="Left" style="font-size: 12px">
      <p>立即注册</p>
      <p>忘记密码?</p>
    </div>
  </el-form-item>
  <el-form-item>
    <el-button  class="Buttonone" >立即登录</el-button>
  </el-form-item>
   <el-form-item>
     <div class="Imgbox">
       <div class="Img">
         <img src="../../assets/login/3.png" alt="">
       </div>
       <div class="Img">
         <img src="../../assets/login/4.png" alt="">
       </div>
       <div class="Img">
         <img src="../../assets/login/5.png" alt="">
       </div>

     </div>
   </el-form-item>
</el-form>
  </div>
</template>

<script>
  export default {
    name: 'Sign',
    props: {
      // msg: String
    },
    methods: {

    },
    data(){
      return{
                form: {
          name: '',
          region: '',
          date1: '',
          date2: '',
          delivery: false,
          type: [],
          resource: '',
          desc: ''
        }
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .Title{
    margin-top: 30px;
  }
  .Title1{
    display: flex;
    justify-content: space-around;
    margin-top: 5px;
    margin-bottom: 35px;
  }
  .Title1 .box{
    display: flex;
    margin-top: 6px;
  }

  .box-one{
    height: 2px;
    width: 60px;
    background-color: #cccccc;
  }
  .box-two{
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background-color: #ccc;
    margin-top: -1.5px;
  }
  .Boxone{
    position: relative;
    left: 0;
    top: 0;
  }
  .Boxtwo{
    position: relative;
    left: 0;
    top: 0;
  }
  .Boxone p{
    height:24px;
    color: #a0a0a0;
    font-size: 12px;
    position: absolute;
    left: 90px;
    top: -18px;
    background: white;
  }
  .Boxtwo p{
    height: 24px;
    color: #a0a0a0;
    font-size: 12px;
    position: absolute;
    left: 90px;
    top: -18px;
    background: white;
  }
  .Left{
    width: 280px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
  }
  .Left p{
    color: #8c8c8c;
  }
  .Buttonone{
    width: 280px;
    background: #7d7d7d;
    color: white;
  }
  .Imgbox{
    width: 180px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
  }
</style>