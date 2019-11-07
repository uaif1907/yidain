<template>
  <div class="detail" style="width:1200px;margin:auto;height:auto;">
    <!-- // 面包屑 -->
    <el-breadcrumb separator="/" class="bread">
      <div class="yuandian1"></div>
      <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item><a href="/">座椅</a></el-breadcrumb-item>
      <el-breadcrumb-item>北欧旅程</el-breadcrumb-item>
    </el-breadcrumb>
    <div class="showbox">
      <div class="showimg">
        <!-- // 大图预览 -->
        <img src="../../assets/details-img/chair1.png" alt="231" style="width:360px;height:450px;">
        <!-- // 小图预览 -->
        <div style="display:flex;justify-content:space-around;margin-top:40px;">
          <div style="width:70px;height:70px;background:#f3f3f3;padding:10px;">
            <img src="../../assets/details-img/chair2.png" alt="" style="width:55px;height:70px;">
          </div>
          <div style="width:90px;height:90px;">
            <img src="../../assets/details-img/chair3.png" alt="" style="width:90px;height:90px;">
          </div>
          <div style="width:90px;height:90px;">
            <img src="../../assets/details-img/chair4.png" alt="" style="width:90px;height:90px;">
          </div>
          <div style="width:90px;height:90px;">
            <img src="../../assets/details-img/chair5.png" alt="" style="width:90px;height:90px;">
          </div>
        </div>
      </div>
      <div class="showtext">
        <!-- // 商品介绍 -->
        <div style="height:20px;float:left;"><img src="../../assets/details-img/text1.png" alt="" style="width:350px;height:20px;"></div>
        <div style="height:20px;float:left;margin-top:20px;"><img src="../../assets/details-img/text2.png" alt="" style="width:300px;height:15px;"></div>
        <div class="yellowline"></div>
        <p class="text1">沙发木框线条柔美，全榫卯结构，细
          <br>节经手工打磨，扶手对接处使用烟袋锅榫，过渡顺滑手感细腻，扶
          <br>手、靠背边缘的屋檐设计更显秀气禅
        </p>
        <p style="text-align:left;padding-top:20px;">
          <span style="font-size:30px;">999.00</span>
          <span style="font-size:13px;padding-left:20px;">RMB</span>
        </p>
        <div style="display:flex;margin-top:25px;height:50px;line-height:40px;">
          <div>颜色分类</div>
          <div style="width:40px;height:40px;border-radius:50%;background-color:#ffc04b;margin-left:20px;"></div>
          <div style="width:40px;height:40px;border-radius:50%;background-color:#e9c7ab;margin-left:20px;"></div>
          <div style="width:40px;height:40px;border-radius:50%;background-color:#caca74;margin-left:20px;"></div>
        </div>
        <div style="margin-top:20px;display:flex;">
          <div style="width:100px;display:flex;height:33px;line-height:33px;">
            <span>数</span>
            <span style="margin-left:36px;">量</span>
          </div>
          <div>
            <el-input-number v-model="num" @change="handleChange" :min="1" :max="10" label="描述文字" size="small"></el-input-number>
          </div>
          <div style="width:100px;display:flex;height:33px;line-height:33px;margin-left:20px;">
            <span>库存{{num1}}件</span>
          </div>
        </div>
        <div style="display:flex;margin-top:40px;">
          <el-button style="width:150px;background-color:#5ed5e0;color:white;boeder-radius:0px;">立即购买</el-button>
          <el-button style="width:150px;margin-left:20px;">加入购物车</el-button>
        </div>
      </div>
    </div>
    <Recommend></Recommend>
  </div>
</template>

<script>
// @ is an alias to /src
import Recommend from '@/components/front-end/recommend/Recommend.vue'

export default {
  name: 'detail',
  components: {
    Recommend,
  },
  data() {
      return {
        num: 1,
        num1:31,
      }
    }
}
</script>
<style scoped>
  .bread{
    padding: 10px;
    font-size:15px;
    margin-top: 40px;
  }
  .showbox{
    width: 100%;
    height:auto;
    display: flex;
    margin-top:60px;
  }
  .showimg{
    width:600px;
    height:100%;
    padding: 10px;
  }
  .showtext{
    width:600px;
    height:auto;
    padding: 40px 0 0 50px;
  }
  .yuandian1{
    float:left;
    width:10px;
    height:10px;
    background-color: #5ed5e0;
    border-radius: 50%;
    margin: 2px 20px;
  }
  .yellowline{
    width:30px;
    height:8px;
    border-radius: 5px;
    background-color: #ffc04b;
    margin-top: 80px;
  }
  .text1{
    text-align: left;
    padding-top: 25px;
    font-size: 12px;
    line-height: 20px;
    color:#979797;
  }
</style>