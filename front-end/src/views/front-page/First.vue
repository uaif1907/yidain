<template>
  <div class="home">
      <template>
          <el-carousel indicator-position="outside" height="500px">
              <el-carousel-item height="500px">
                  <div class="role_1">
                      <div class="buy">
                          立即购买
                      </div>
                  </div>
              </el-carousel-item>
              <el-carousel-item height="500px">
                  <div class="role_2">
                  </div>
              </el-carousel-item>
          </el-carousel>
      </template>
      <div style="font-size: 25px"><span style="font-weight: bold;color:#ffca57;">－</span>&nbsp;新品首发&nbsp;<span style="font-weight:bold;color:#ffca57">－</span></div>
    <!--第二行-->
      <div class="line2">
        <div class="left">
            <div></div>
        </div>
        <div class="right">
            <div class="right_one">
                HENRIKSDAL 亨利克
                <div class="row"></div>
                椅子，桦木，格雷伯 白色
                <br>
                愉快地想用完漫长的餐点后，如果桌布
                <br>
                椅子可以清洗，那可正式美事一桩
                <br>
                HENRIKSDL 亨利克
                <br>
                可能是我们最舒适的椅子了
            </div>
        </div>
      </div>

      <!--第二行结束-->
    <div>dsd</div>
     <div>dsd</div>
     <div>dsd</div>
     <div>dsd</div>
     <div>dsd</div>
     <div>dsd</div>
     <div>dsd</div>
     <div>dsd</div>
     <div>dsd</div>
  </div>
</template>
<style>
    .role_1{
        background:url('../../assets/firstpage_need_png/first.png') no-repeat;
        background-size: cover;
        width:1200px;
        height:500px;
        position:relative;

    }
    .buy{
        width:180px;
        height:50px;
        background:white;
        color:#358c94;
        position:absolute;
        left:180px;
        line-height:50px;
        bottom:50px;
    }
    .role_2{
        background:url('../../assets/firstpage_need_png/first_1.png') no-repeat;
        background-size: cover;
        width:1200px;
        height:500px;
    }
    .line2{
        width:1200px;
        height:500px;
    }
    .left{
        width:600px;
        height:500px;
        float:left;
        position:relative;
    }
    .left div{
        background:url("../../assets/firstpage_need_png/second.png") no-repeat ;
        background-size:cover;
        width:400px;
        position:absolute;
        height:400px;
        right:0;

    }
    .right{
        width:600px;
        height:500px;
        float:left;
        position:relative;
        padding-top:70px;

    }
    .right_one{
        width:300px;
        height:200px;
        margin:0 auto;
        line-height:200px;
        background:green;
        text-align:left;
    }
    .row{
        margin-top:-65px;
        width:30px;
        height:2px;
        background:#ffca57;
    }



  .el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 300px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>
<script>
// @ is an alias to /src


export default {
  name: 'home',
  components: {

  }
}
</script>
