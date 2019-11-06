<template>
  <div class="success" style="width: 1200px;margin: 0 auto">
      <div style="width: 860px;height: 55px;margin: 140px auto;margin-bottom:0;background: #f4f4f4;position: relative">
          <span style="position: absolute;left: 0;right: 0;top:-27px; color: #999;font-size:50px">· SUCCESS ·</span>
          <img src="../../../assets/shopcart/图层60.png" alt="" style="position: absolute;left:-30px;z-index: -1">
      </div>
      <div style="width: 670px;margin: 0 auto;text-align: center;">
          <p style="font-weight: 600">恭喜您，支付成功啦～～</p>
          <p style="line-height: 80px">您的订单号是</p>
          <p  style="font-weight: 800;font-size: 20px">2019042814458299</p>
      </div>
      <div style="margin-top: 100px;margin-bottom: 80px">
          <el-row>
              <el-button size="medium" type="info" plain>查看订单</el-button>
              <el-button size="medium" type="info" plain>还想看看</el-button>
          </el-row>

      </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'success',
  components: {
    // HelloWorld
  }
}
</script>