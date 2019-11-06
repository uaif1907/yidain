<template>
  <div class="recommends">
    <div class="bidbox">
        <div class="top">
            <img src="../../../assets/recommend-img/topback.png" alt="" style="width:400px;height:90px;">
        </div>
        <div class="fourbox">
          <div class="four">
            <div class="shopcar"><i class="el-icon-shopping-cart-1"></i></div>
            <div>
              <img src="../../../assets/recommend-img/chair1.png" alt="" style="width:150px;height:200px;margin:20px 0 10px 16px;">
            </div>
            <div class="yellowline"></div>
            <div class="center" style="color:#887;">OBEDIENCE FUJIJO</div>
            <div class="center text1"><span style="color:#dbdbdb">^</span> 海螺椅 <span style="color:#dbdbdb">^</span></div>
            <div class="center text2">现代小椅，随处安放的舒适</div>
            <div class="center" style="display:flex;padding-left:80px;">
              <div style="font-size:3px;color:#979797;">RMB</div>
              <div style="font-size:20px;">460. 00</div>
            </div>
          </div>
          <div class="four">
            <div class="shopcar"><i class="el-icon-shopping-cart-1"></i></div>
            <div>
              <img src="../../../assets/recommend-img/chair2.png" alt="" style="width:150px;height:200px;margin:20px auto;">
            </div>
            <div class="yellowline"></div>
            <div class="center" style="color:#887;">OBEDIENCE FUJIJO</div>
            <div class="center text1"><span style="color:#dbdbdb">^</span> 青山椅 <span style="color:#dbdbdb">^</span></div>
            <div class="center text2">抽离繁琐的设计，体现美的线条</div>
            <div class="center" style="display:flex;padding-left:80px;">
              <div style="font-size:3px;color:#979797;">RMB</div>
              <div style="font-size:20px;">540. 00</div>
            </div>
          </div>
          <div class="four">
            <div class="shopcar"><i class="el-icon-shopping-cart-1"></i></div>
            <div>
              <img src="../../../assets/recommend-img/chair3.png" alt="" style="width:150px;height:200px;margin:20px 25px 20px 0;">
            </div>
            <div class="yellowline"></div>
            <div class="center" style="color:#887;">OBEDIENCE FUJIJO</div>
            <div class="center text1"><span style="color:#dbdbdb">^</span> 藤条椅 <span style="color:#dbdbdb">^</span></div>
            <div class="center text2">设计简单而不失尊贵</div>
            <div class="center" style="display:flex;padding-left:80px;">
              <div style="font-size:3px;color:#979797;">RMB</div>
              <div style="font-size:20px;">630. 00</div>
            </div>
          </div>
          <div class="four">
            <div class="shopcar"><i class="el-icon-shopping-cart-1"></i></div>
            <div>
              <img src="../../../assets/recommend-img/chair4.png" alt="" style="width:150px;height:200px;margin:20px auto;">
            </div>
            <div class="yellowline"></div>
            <div class="center" style="color:#887;">OBEDIENCE FUJIJO</div>
            <div class="center text1"><span style="color:#dbdbdb">^</span> 网红椅 <span style="color:#dbdbdb">^</span></div>
            <div class="center text2">无任何人造板和贴皮</div>
            <div class="center" style="display:flex;padding-left:80px;">
              <div style="font-size:3px;color:#979797;">RMB</div>
              <div style="font-size:20px;">250. 00</div>
            </div>
          </div>
        </div>
        <div style="width:100%;height:120px;"></div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'recommends',
  components: {
    
  }
}
</script>
<style scoped>
  .bigbox{
    width:100%;
    height:100%;
  }
  .top{
    width:500px;
    height: 150px;
    padding-top: 100px;
    margin: auto;
  }
  .fourbox{
    display: flex;
    justify-content: space-around;
  }
  .four{
    width:250px;
    height:420px;
    text-align: center;
    border:3px solid #fff;
    position: relative;
    cursor: pointer;
  }
  .four:hover{
    background-color: #f3f3f3;
    box-shadow: 0px 0px 6px 0px;
  }
  .shopcar{
    font-size: 24px;
    position: absolute;
    top: 10px;
    left:10px;
    display: none;
  }
  .four:hover .shopcar{
    display: block;
  }
  .yellowline{
    width:40px;
    height:8px;
    border-radius: 6px;
    background-color:#ffca57;
    margin: 20px auto;
  }
  .center{
    margin:12px auto;
  }
  .text1{
    font-size: 18px;
    color:black;
  }
  .text2{
    font-size: 12px;
    color:#979797;
  }
</style>