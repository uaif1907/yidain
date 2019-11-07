<template>
  <div class="list-box">
      <Cabinet></Cabinet>
  </div>
</template>

<script>
  // @ is an alias to /src
    import Cabinet from '@/components/front-end/List/Cabinet.vue'

  export default {
    name: 'lists',
    components: {
        Cabinet
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
    background: url("../../assets/list/lb1.png") no-repeat;
    background-size: 100% 100%;
  }
  .el-carousel__item:nth-child(2n) {
    background: url("../../assets/list/lb2.png") no-repeat;
    background-size: cover;
  }
  .el-carousel__item:nth-child(3) {
    background: url("../../assets/list/lb3.png") no-repeat;
    background-size: cover;
  }
  .el-carousel__item:nth-child(4){
    background: url("../../assets/list/lb4.png") no-repeat;
    background-size: cover;
  }
  .banner-box{
    height: 500px!important;
  }
  .el-carousel__container{
    height: 500px!important;
  }
</style>
