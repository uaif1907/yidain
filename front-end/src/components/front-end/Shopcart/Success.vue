<template>
  <div class="success" style="width: 1200px;margin: 0 auto">
      <div style="width: 670px;height: 60px;margin: 0 auto;background: #f4f4f4">
          <span>· SUCCESS ·</span>
          <img src="../../../assets/shopcart/图层60.png" alt="">
      </div>
      <div style="width: 670px;margin: 0 auto;text-align: center">
          <p>恭喜您，支付成功啦～～</p>
          <p>您的订单号是</p>
          <p>2019042814458299</p>
      </div>
      <div>
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