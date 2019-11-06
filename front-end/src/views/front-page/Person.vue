<template>
  <div class="person-box">
    <!-- 这里是头部面包屑 -->
    <div class="crumbs">
      <div class="index-person">
        <div class="yuan"></div>
        <div class="crumbs-wz">首页 / 个人中心</div>
      </div>
    </div>
    <!-- 这里是主体哦 -->
    <div class="person-main">

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
    height: 205px;
    /*background-color: #2c3e50;*/
    padding-top: 40px;
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
  .index-person .crumbs-wz  {
    font-size: 16px;
    color: #191919;
    height: 50px;
    float: left;
    font-weight: 600;
    line-height: 50px;
    margin-left: 10px;
  }
  .person-main{
    width: 1200px;
    height: ;
  }
</style>