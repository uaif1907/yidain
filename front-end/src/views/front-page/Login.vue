<template>
  <div class="home">
    <div class="blockone">
      <el-carousel style="width: 1519.2px;height: 500px">
        <el-carousel-item>
          <div class="Img1" style="width: 1519.2px;height: 500px"></div>
        </el-carousel-item>
        <el-carousel-item>
        <div class="Img2" style="width: 1519.2px;height: 500px"></div>
        </el-carousel-item>
    </el-carousel>
      <div class="pos">
        <Sign></Sign>
      </div>
      <div class="pos2">
        <Register></Register>
      </div>
    </div>

  </div>
</template>

<script>
// @ is an alias to c
import Sign from '@/components/Sign/sign.vue'
import Register from '@/components/Register/register.vue'

export default {
  name: 'home',
  components: {
    Sign,
    Register,
  },
  data(){
    return{
      // imagesbox:[{
      //   id:1,
      //   src:'../../assets/login/1.png'
      // },
      //   {
      //     id:2,
      //     src:'../../assets/login/2.png'
      //   }
      // ]

    }
  }
}
</script>
<style scoped>
/*img{*/
/*  width: 100%;*/
/*  height: 100%;*/
/*}*/
  .blockone{
    position: relative;
    left: 0;
    top: 0;
  }
  .pos{
    width: auto;
    height: auto;
    position: absolute;
    right: 100px;
    top: 60px;
    z-index: 50;
  }
    .pos2{
    width: auto;
    height: auto;
    position: absolute;
    right: 100px;
    top: 60px;
    z-index: 40;
  }
  .Img1{
    background: url("../../assets/login/1.png");
  }
  .Img2{
    background: url("../../assets/login/2.png");
  }

</style>