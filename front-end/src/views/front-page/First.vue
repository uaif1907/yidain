<template>
  <div class="home" style="width:1200px;margin:0 auto;;height:auto;">
      <div>
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
                      <div class="buy">
                          立即购买
                      </div>
                  </div>
              </el-carousel-item>
              <el-carousel-item height="500px">
                  <div class="role_3">
                      <div class="buy">
                          立即购买
                      </div>
                  </div>
              </el-carousel-item>
              <el-carousel-item height="500px">
                  <div class="role_4">
                      <div class="buy">
                          立即购买
                      </div>
                  </div>
              </el-carousel-item>
          </el-carousel>
      </template>
      </div>
      <div style="font-size: 25px;margin-top:60px;"><span style="font-weight: bold;color:#ffca57;">－</span>&nbsp;<b>新品首发</b>&nbsp;<span style="font-weight:bold;color:#ffca57">－</span></div>
      <div style="font-size: 25px;"><b style="color:#7f7f7f;">NEW PRODUCT STARTER</b></div>
      <div style="margin-bottom:30px"><h6>属于你的就是最新的</h6></div>
      <!--第二行-->
      <div class="line2">
        <div class="left">
            <div></div>
        </div>
        <div class="right">
            <div class="right_one">
                <h2 v-text="lines[0].source"></h2>
                <div class="row"></div>
                <h3 style="color:#798989" v-text="lines[0].descript" ></h3>
                <br>
                <span style="color:#797979">愉快地想用完漫长的餐点后，如果桌布</span>
                <br>
                <span style="color:#797979">椅子可以清洗，那可正式美事一桩HENRIKSDL&nbsp;亨利克&nbsp;可能</span>
                <br>
                <span style="color:#797979">是我们最舒适的椅子了!</span>
                <div style="margin-top:30px;margin-bottom:20px">
                    RMB&nbsp;<span style="font-size:35px;" v-text="lines[0].price"><b>499</b></span>
                </div>
                <button style="border:1px solid black;width:45px;height:20px;outline: none;cursor: pointer;background-color: transparent" @click="clickk(lines[0].source)">Buy</button>
            </div>
        </div>
      </div>
      <div class="flower" >
        <div ></div>
      </div>
      <!--第二行结束-->
      <!--第三行开始-->
      <div class="line3">
        <div class="line3_left">
            <span style="font-size:45px;position:absolute;right:-105px;top:50px;"><b v-text="lines[1].source" ></b></span>
            <div style="position:absolute;top:110px">
                <p style="font-size:30px;" v-text="lines[1].descript"></p>
                <br>
                <p style="font-size:30px;">沙发套可选</p>
                <br>
                <p>这是一款非常棒的椅子，采用曲木设计，结</p>
                <p>实耐用，十分灵活，都贴合人体曲线，打造理想舒适感</p>
                <br>
                RMB&nbsp;<span style="font-size: 30px" v-text="lines[1].price"></span>
                <br>
                <br>
                <button style="border:1px solid black;width:45px;height:20px;background-color:transparent;outline: none;cursor: pointer" @click="clickk(lines[1].source)">Buy</button>
            </div>
        </div>
        <div  class="line3_right"></div>
    </div>
      <!--第三行结束-->
      <div style="margin-top:80px;width:1200px;height:100px;text-align: center;position:relative">
          <span style="position:absolute;left:0;right:0;font-size: 25px;color:#ffca57;">－&nbsp;<b style="color:black">人气推荐</b>&nbsp;－</span>
          <span style="position:absolute;left:0;right:0;font-size: 25px;top:30px;"><b style="color:#7f7f7f;">PRODUCT TESTIMONIALS</b></span>
          <span style="position:absolute;left:0;right:0;font-size: 12px;top:60px;"><b>把最好的都给你</b></span>
      </div>
      <!--第四行开始-->
      <div class=" line4">
         <div class="line4_left" >
             <div>
                 <span style="position:absolute;left:2px;top:62px;font-size:14px"><b v-text="lines[2].source"></b></span>
                 <span style="position:absolute;left:-55px;top:85px;font-size:15px"><b>SODERHNMAN</b></span>
                 <span style="position:absolute;left:-40px;top:120px;font-size:10px" v-text="lines[2].descript"></span>
                 <p style="position:absolute;left:-35px;top:145px;font-size:10px">RMB</p><span style="position:absolute;left:0;top:140px;font-size:17px"><b v-text="lines[2].price"></b></span>
                 <button style="border:1px solid black;width:45px;height:20px;position:absolute;left:10px;top:175px;outline: none;cursor: pointer;background-color: transparent" @click="clickk(lines[2].source)">Buy</button>
             </div>
         </div>
         <div class="line4_right">
             <div>
                 <span style="position:absolute;right:-2px;top:170px;font-size:14px"><b v-text="lines[3].source"></b></span>
                 <span style="position:absolute;right:-18px;top:190px;font-size:14px"><b>ANTIFONI</b></span>
                 <span style="position:absolute;right:-44px;top:220px;font-size:10px" v-text="lines[3].descript"></span>
                 <p style="position:absolute;right:25px;top:250px;font-size:10px">RMB</p><span style="position:absolute;right:-35px;top:245px;font-size:17px"><b v-text="lines[3].price"></b></span>
                 <button style="border:1px solid black;width:45px;height:20px;position:absolute;right:2px;top:270px;outline: none;cursor: pointer;background-color: transparent" @click="clickk(lines[3].source)">Buy</button>
             </div>
         </div>
     </div>
      <!--第四行结束-->
      <!--第五行开始-->
      <div class="line5">
          <div class="line5_left"></div>
          <div class="line5_right">
              <div class = "five" style="text-align: left;">
                  <p style="color:#ffca57;font-size: 15px;"><b>－</b></p>
                  <p><b v-text="lines[4].source"></b></p>
                  <p style="font-size: 10px;">Give you a truly relaxing and comfortable experience</p>
              </div>
              <div class="five_2" style="position:absolute;">
                  <p><b v-text="lines[4].descript"></b></p>
                  <br>
                  <p>这款高靠背座椅为颈部提供额外支撑，给你带来真正</p>
                  <p>放松的数是体验，表面柔软，紧致厚实，具有反光效果</p>
                  <span style="font-size: 10px">RMB&nbsp;</span><span><b v-text="lines[4].price">499.00</b></span>
                  <br>
                  <button style="border:1px solid black;width:45px;height:20px;outline: none;cursor: pointer;background-color: transparent" @click="clickk(lines[4].source)">Buy</button>
              </div>
          </div>
      </div>
      <!--第五行结束-->
      <div>
          <div style="font-size: 25px;margin-top:60px;"><span style="font-weight: bold;color:#ffca57;">－</span>&nbsp;<b>今日特价</b>&nbsp;<span style="font-weight:bold;color:#ffca57">－</span></div>
          <div style="font-size: 25px;"><b style="color:#7f7f7f;">PRODUCT TESTIMONIALS</b></div>
          <div style="margin-bottom:30px"><h6>把最好的都给你</h6></div>
      </div>
      <!--第六行开始-->
      <div class="line6">
          <div style="width:25px;color:darkgrey;height:450px;line-height:300px;"><span style="cursor: pointer" @click="left">←</span></div>
          <div class="line6_div" v-if="present===1">
              <div class="line6_1" :data="rows[0]">
                  <span style="display:block;border-radius:50%;width:60px;height:60px;background-color:yellow;position:absolute;top:20px;left:-15px;font-size:20px;text-align: center;line-height: 60px;opacity: 0.6"><b>SALE</b></span>
                  <span style="position:absolute;bottom:0;left:0;font-size:10px;">
                      RMB
                      <span style="font-size: 20px"><b v-text="rows[0].price"></b></span>
                  </span>
                  <span style="border:1px solid black;width:45px;height:15px;position:absolute;bottom:0;font-size:13px;right:0;cursor:pointer" @click="clickk(rows[0].source)">Buy</span>
              </div>
              <div class="line6_2">
                  <span style="display:block;border-radius:50%;width:60px;height:60px;background-color:yellow;position:absolute;top:20px;left:-15px;font-size:20px;text-align: center;line-height: 60px;opacity: 0.6"><b>SALE</b></span>
                  <span style="position:absolute;bottom:0;left:0;font-size:10px;">
                      RMB
                      <span style="font-size: 20px"><b v-text="rows[1].price"></b></span>
                  </span>
                  <span style="border:1px solid black;width:45px;height:15px;position:absolute;bottom:0;font-size:13px;right:0;cursor:pointer" @click="clickk(rows[1].source)">Buy</span>
              </div>
              <div class="line6_3">
                  <span style="display:block;border-radius:50%;width:60px;height:60px;background-color:yellow;position:absolute;top:20px;left:-15px;font-size:20px;text-align: center;line-height: 60px;opacity: 0.6"><b>SALE</b></span>
                  <span style="position:absolute;bottom:0;left:0;font-size:10px;">
                      RMB
                      <span style="font-size: 20px"><b v-text="rows[2].price"></b></span>
                  </span>
                 <span style="border:1px solid black;width:45px;height:15px;position:absolute;bottom:0;font-size:13px;right:0;cursor:pointer" @click="clickk(rows[2].source)">Buy</span>
              </div>
              <div class="line6_4">
                  <span style="display:block;border-radius:50%;width:60px;height:60px;background-color:yellow;position:absolute;top:20px;left:-15px;font-size:20px;text-align: center;line-height: 60px;opacity: 0.6"><b>SALE</b></span>
                  <span style="position:absolute;bottom:0;left:0;font-size:10px;">
                      RMB
                      <span style="font-size: 20px"><b v-text="rows[3].price"></b></span>
                  </span>
                  <span style="border:1px solid black;width:45px;height:15px;position:absolute;bottom:0;font-size:13px;right:0;cursor:pointer" @click="clickk(rows[3].source)">Buy</span>
              </div>
          </div>
          <div class="line6_div" v-else-if="present===2">
              <div class="line6_2">
                  <span style="display:block;border-radius:50%;width:60px;height:60px;background-color:yellow;position:absolute;top:20px;left:-15px;font-size:20px;text-align: center;line-height: 60px;opacity: 0.6"><b>SALE</b></span>
                  <span style="position:absolute;bottom:0;left:0;font-size:10px;">
                      RMB
                      <span style="font-size: 20px"><b v-text="rows[1].price"></b></span>
                  </span>
                  <span style="border:1px solid black;width:45px;height:15px;position:absolute;bottom:0;font-size:13px;right:0;cursor:pointer" @click="clickk(rows[1].source)">Buy</span>
              </div>
              <div class="line6_1" :data="rows[0]">
                  <span style="display:block;border-radius:50%;width:60px;height:60px;background-color:yellow;position:absolute;top:20px;left:-15px;font-size:20px;text-align: center;line-height: 60px;opacity: 0.6"><b>SALE</b></span>
                  <span style="position:absolute;bottom:0;left:0;font-size:10px;">
                      RMB
                      <span style="font-size: 20px"><b v-text="rows[0].price"></b></span>
                  </span>
                  <span style="border:1px solid black;width:45px;height:15px;position:absolute;bottom:0;font-size:13px;right:0;cursor:pointer" @click="clickk(rows[0].source)">Buy</span>
              </div>
              <div class="line6_3">
                  <span style="display:block;border-radius:50%;width:60px;height:60px;background-color:yellow;position:absolute;top:20px;left:-15px;font-size:20px;text-align: center;line-height: 60px;opacity: 0.6"><b>SALE</b></span>
                  <span style="position:absolute;bottom:0;left:0;font-size:10px;">
                      RMB
                      <span style="font-size: 20px"><b v-text="rows[2].price"></b></span>
                  </span>
                 <span style="border:1px solid black;width:45px;height:15px;position:absolute;bottom:0;font-size:13px;right:0;cursor:pointer" @click="clickk(rows[2].source)">Buy</span>
              </div>
              <div class="line6_4">
                  <span style="display:block;border-radius:50%;width:60px;height:60px;background-color:yellow;position:absolute;top:20px;left:-15px;font-size:20px;text-align: center;line-height: 60px;opacity: 0.6"><b>SALE</b></span>
                  <span style="position:absolute;bottom:0;left:0;font-size:10px;">
                      RMB
                      <span style="font-size: 20px"><b v-text="rows[3].price"></b></span>
                  </span>
                  <span style="border:1px solid black;width:45px;height:15px;position:absolute;bottom:0;font-size:13px;right:0;cursor:pointer" @click="clickk(rows[3].source)">Buy</span>
              </div>
          </div>
          <div class="line6_div" v-else-if="present===3">
              <div class="line6_3">
                  <span style="display:block;border-radius:50%;width:60px;height:60px;background-color:yellow;position:absolute;top:20px;left:-15px;font-size:20px;text-align: center;line-height: 60px;opacity: 0.6"><b>SALE</b></span>
                  <span style="position:absolute;bottom:0;left:0;font-size:10px;">
                      RMB
                      <span style="font-size: 20px"><b v-text="rows[2].price"></b></span>
                  </span>
                 <span style="border:1px solid black;width:45px;height:15px;position:absolute;bottom:0;font-size:13px;right:0;cursor:pointer" @click="clickk(rows[2].source)">Buy</span>
              </div>
              <div class="line6_2">
                  <span style="display:block;border-radius:50%;width:60px;height:60px;background-color:yellow;position:absolute;top:20px;left:-15px;font-size:20px;text-align: center;line-height: 60px;opacity: 0.6"><b>SALE</b></span>
                  <span style="position:absolute;bottom:0;left:0;font-size:10px;">
                      RMB
                      <span style="font-size: 20px"><b v-text="rows[1].price"></b></span>
                  </span>
                  <span style="border:1px solid black;width:45px;height:15px;position:absolute;bottom:0;font-size:13px;right:0;cursor:pointer" @click="clickk(rows[1].source)">Buy</span>
              </div>
              <div class="line6_1" :data="rows[0]">
                  <span style="display:block;border-radius:50%;width:60px;height:60px;background-color:yellow;position:absolute;top:20px;left:-15px;font-size:20px;text-align: center;line-height: 60px;opacity: 0.6"><b>SALE</b></span>
                  <span style="position:absolute;bottom:0;left:0;font-size:10px;">
                      RMB
                      <span style="font-size: 20px"><b v-text="rows[0].price"></b></span>
                  </span>
                  <span style="border:1px solid black;width:45px;height:15px;position:absolute;bottom:0;font-size:13px;right:0;cursor:pointer" @click="clickk(rows[0].source)">Buy</span>
              </div>
              <div class="line6_4">
                  <span style="display:block;border-radius:50%;width:60px;height:60px;background-color:yellow;position:absolute;top:20px;left:-15px;font-size:20px;text-align: center;line-height: 60px;opacity: 0.6"><b>SALE</b></span>
                  <span style="position:absolute;bottom:0;left:0;font-size:10px;">
                      RMB
                      <span style="font-size: 20px"><b v-text="rows[3].price"></b></span>
                  </span>
                  <span style="border:1px solid black;width:45px;height:15px;position:absolute;bottom:0;font-size:13px;right:0;cursor:pointer" @click="clickk(rows[3].source)">Buy</span>
              </div>
          </div>
          <div class="line6_div" v-else-if="present===4">
              <div class="line6_4">
                  <span style="display:block;border-radius:50%;width:60px;height:60px;background-color:yellow;position:absolute;top:20px;left:-15px;font-size:20px;text-align: center;line-height: 60px;opacity: 0.6"><b>SALE</b></span>
                  <span style="position:absolute;bottom:0;left:0;font-size:10px;">
                      RMB
                      <span style="font-size: 20px"><b v-text="rows[3].price"></b></span>
                  </span>
                  <span style="border:1px solid black;width:45px;height:15px;position:absolute;bottom:0;font-size:13px;right:0;cursor:pointer" @click="clickk(rows[3].source)">Buy</span>
              </div>
              <div class="line6_3">
                  <span style="display:block;border-radius:50%;width:60px;height:60px;background-color:yellow;position:absolute;top:20px;left:-15px;font-size:20px;text-align: center;line-height: 60px;opacity: 0.6"><b>SALE</b></span>
                  <span style="position:absolute;bottom:0;left:0;font-size:10px;">
                      RMB
                      <span style="font-size: 20px"><b v-text="rows[2].price"></b></span>
                  </span>
                 <span style="border:1px solid black;width:45px;height:15px;position:absolute;bottom:0;font-size:13px;right:0;cursor:pointer" @click="clickk(rows[2].source)">Buy</span>
              </div>
              <div class="line6_2">
                  <span style="display:block;border-radius:50%;width:60px;height:60px;background-color:yellow;position:absolute;top:20px;left:-15px;font-size:20px;text-align: center;line-height: 60px;opacity: 0.6"><b>SALE</b></span>
                  <span style="position:absolute;bottom:0;left:0;font-size:10px;">
                      RMB
                      <span style="font-size: 20px"><b v-text="rows[1].price"></b></span>
                  </span>
                  <span style="border:1px solid black;width:45px;height:15px;position:absolute;bottom:0;font-size:13px;right:0;cursor:pointer" @click="clickk(rows[1].source)">Buy</span>
              </div>
              <div class="line6_1" :data="rows[0]">
                  <span style="display:block;border-radius:50%;width:60px;height:60px;background-color:yellow;position:absolute;top:20px;left:-15px;font-size:20px;text-align: center;line-height: 60px;opacity: 0.6"><b>SALE</b></span>
                  <span style="position:absolute;bottom:0;left:0;font-size:10px;">
                      RMB
                      <span style="font-size: 20px"><b v-text="rows[0].price"></b></span>
                  </span>
                  <span style="border:1px solid black;width:45px;height:15px;position:absolute;bottom:0;font-size:13px;right:0;cursor:pointer" @click="clickk(rows[0].source)">Buy</span>
              </div>
          </div>
          <div style="width:25px;color:darkgrey;height:450px;line-height:300px"><span style="cursor:pointer" @click="right">→</span></div>
      </div>
      <div style="position:relative">
          <span style="font-size: 35px;"><span style="font-size:13px;color:lightgray;line-height: 35px;position:absolute;right:620px">←</span>{{present}}<span style="font-size: 10px;color:lightgray;position:absolute;">/4</span>&nbsp;&nbsp;&nbsp;<span style="font-size:13px;color:lightgray;position:absolute;top:10px">→</span></span>
      </div>
      <!--第六行结束-->
      <!--第七行开始-->
      <div class="line7">
          <div style="text-align: left;margin-left:100px;" class="line7_left">
              <div style="margin-top:80px;width:400px;height:200px;" :model="Time.hour">
                  <p style="color:#4edbff;font-size: 40px">LIMITED-TIME SHOPPING</p>
                  <p style="color:#4edbff;font-size: 25px" >限时抢购</p>
                  <span><span><b style="font-size: 35px;color:#4edbff">{{hour}}</b>小时</span><span><b style="font-size: 35px;color:#4edbff">{{minute}}</b>分</span><span><b style="font-size: 35px;color:#4edbff">{{sec}}</b>秒</span></span>
                  <br>
                  <p>免费配送，优惠折扣，更优惠更实用，等你来抢购</p>
                  <br>
                  <p>Free shopping.Discount,more favorable more practical,waiting for</p>
                  <p>you to buy</p>
              </div>

              <div style="width:150px;height:30px;text-align:center;line-height: 30px;font-size:25px;position:absolute;bottom:50px;background:#4edbff;color:white;cursor:pointer" @click="clickk('立即抢购')">
                  立即抢购
              </div>

          </div>

            <div class="line7_right">
                <div class="img1"></div>
                <div class="img2"></div>
            </div>

      </div>
      <!--第七行结束-->
      <!--关于我们-->
      <div>
          <div style="font-size: 25px;margin-top:60px;"><span style="font-weight: bold;color:#ffca57;">－</span>&nbsp;<b>关于我们</b>&nbsp;<span style="font-weight:bold;color:#ffca57">－</span></div>
          <div style="font-size: 25px;"><b style="color:#7f7f7f;">ABOUT US</b></div>
          <div style="margin-bottom:30px"><h6>优质服务送给上帝</h6></div>
          <div>
              <p>家具是指人类维持正常生活，是必不可少的家居设施大类。家具也跟随</p>
              <p>时代的脚步不断发展创新，到如今种类繁多，用料各异，品种齐全，用途不一。是建立工作生活空间的重要基础。</p>
              <br>
              <p style="font-size:15px;color:lightgray">Funiture to human beings to maintain life.engage in production practice and</p>
              <p style="font-size:15px;color:lightgray">carry outsocial activities Essential appliance facilities in categories,Furniture also follows the footsteps of the Times to continue to develop and innovate.</p>
              <p style="font-size:15px;color:lightgray">to today a wide range of materials Different.variety complete,different uses.</p>
          </div>
      </div>
      <div style="margin-top:100px;margin-bottom:200px">
          <div class="more" style="font-size: 25px; border:1px solid lightgray;width:150px;height:30px;margin:0 auto;text-align: center;line-height: 30px;cursor:pointer" @click="clickk('MORE')"><b>MORE</b></div>
      </div>
      <!--关于我们-->
  </div>
</template>
<style>
    .role_1{
        background:url('../../assets/firstpage_need_png/lb1.png') no-repeat;
        background-size: cover;
        width:1200px;
        height:500px;
        position:relative;

    }
    .buy{
        width:180px;
        height:50px;
        background:rgba(255,255,255,0.5);
        color:#358c94;
        position:absolute;
        left:180px;
        line-height:50px;
        bottom:50px;
        cursor:pointer;
    }
    .role_2{
        background:url('../../assets/firstpage_need_png/lb2.png') no-repeat;
        background-size: cover;
        width:1200px;
        height:500px;
    }
    .role_3{
        background:url('../../assets/firstpage_need_png/lb3.png') no-repeat;
        background-size: cover;
        width:1200px;
        height:500px;
    }
    .role_4{
        background:url('../../assets/firstpage_need_png/lb4.png') no-repeat;
        background-size: cover;
        width:1200px;
        height:500px;
    }
    .line2{
        width:1200px;
        height:500px;
        position:relative;
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
        width:450px;
        height:300px;
        margin:0 auto;
        text-align:left;
    }
    .row{
        width:30px;
        height:2px;
        margin-top:15px;
        margin-bottom:15px;
        background:#ffca57;
    }
    .flower{
        position:relative;
        top:-150px;
        width:160px;
        height:160px;
        border-radius: 50%;
        background:#fada95;
        margin:0 auto;
    }
    .flower div{
        background:url("../../assets/firstpage_need_png/flower.png") no-repeat center;
        z-index:80;
        width:130px;
        height:140px;
        margin:0 auto;
    }
    .line3{
        width:1200px;
        margin:0 auto;
        height:400px;
    }
    .line3_left{
        width:400px;
       float:left;
         height:600px;
        text-align:right;
        position:relative;
    }
    .line3_right{
        float:left;
        background:url("../../assets/firstpage_need_png/third.png") no-repeat center;
         width:800px;
        height:400px;
    }
    .line4{
        margin:0 auto;
        width:1200px;
        height:400px;
        display:flex;
        flex-wrap:nowrap;
        justify-content:space-between;
        position:relative;
    }
    .line4_left{
        width:600px;
        height:400px;
        position:relative;

    }
    .line4_left div{
        background:url("../../assets/firstpage_need_png/forth_left.png") no-repeat center;
        background-size: cover;
        position:absolute;
        right:0;
        top:70px;
        width:260px;
        height:260px;
    }
    .line4_right{
        width:575px;
        margin-left:25px;
        height:400px;
        position:relative;

    }
    .line4_right div{
        background:url("../../assets/firstpage_need_png/forth_right.png") no-repeat center;
        background-size: cover;
        width:300px;
        position:absolute;
        height:400px;
    }
    .line5{
        margin-top:70px;
        width:1200px;
        height:400px;
    }
    .line5_left{
        width:400px;
        height:400px;
        float:left;
        background:url("../../assets/firstpage_need_png/fifth.png") no-repeat center;
        background-size: cover;
    }
    .line5_right{
        width:800px;
        height:400px;
        float:left;
        text-align: left;
        position:relative;
    }
    .five{
        width:500px;
        height:70px;
        position:absolute;
        left:-100px;
        background-color:white;
        box-shadow: 0 1px 1px darkgrey;
        top:140px;
    }
    .five_2{
        width:500px;
        height:70px;
        position:absolute;
        top:230px;
    }
    .line6{
        width:1200px;
        height:450px;
        display:flex;
        flex-wrap: nowrap;
        justify-content:space-between;
    }
    .line6_div{
        margin:0 auto;
        width:900px;
        height:400px;
        display:flex;
        flex-wrap: nowrap;
        justify-content:space-between
    }
    .line6_1{
        width:160px;
        position:relative;
        background:url("../../assets/firstpage_need_png/sixth_2.png") no-repeat  0 -30px;
        background-size: cover;
        height:300px;

    }
    .line6_1:hover{
        width:160px;
        position:relative;
        background:url("../../assets/firstpage_need_png/sixth_2.png") no-repeat 0 -30px;
        background-size: cover;
        height:330px;
    }
    .line6_2{
        width:160px;
        position:relative;
        background:url("../../assets/firstpage_need_png/sixth_3.png") no-repeat 0 -30px;
        background-size: cover;
        height:300px;
    }
    .line6_2:hover{
         width:160px;
        position:relative;
        background:url("../../assets/firstpage_need_png/sixth_3.png") no-repeat 0 -30px;
        background-size: cover;
        height:330px;
    }
    .line6_3{
        width:160px;
        position:relative;
        background:url("../../assets/firstpage_need_png/sixth_4.png") no-repeat 0 -30px;
        background-size: cover;
        height:300px;
    }
    .line6_3:hover{
        width:160px;
        position:relative;
        background:url("../../assets/firstpage_need_png/sixth_4.png") no-repeat 0 -30px;
        background-size: cover;
        height:330px;
    }
    .line6_4{
        width:160px;
        position:relative;
        background:url("../../assets/firstpage_need_png/sixth_2.png") no-repeat 0 -30px;
        background-size: cover;
        height:300px;
    }
    .line6_4:hover{
        width:160px;
        position:relative;
        background:url("../../assets/firstpage_need_png/sixth_2.png") no-repeat 0 -30px;
        background-size: cover;
        height:330px;
    }
    .line7{
        width:1200px;
        height:450px;
        margin-top:150px;
        background:url('../../assets/firstpage_need_png/bottom.png') no-repeat 0;
        background-size: cover;
        position:relative;

    }
    .line7_left{
         width:600px;
        float:left;
        position:relative;
        height:450px;
    }
    .line7_right{
        /*width:600px;*/
        float:left;
        height:450px;
        position:relative;
    }
    .img1{
        position:absolute;
        background:url('../../assets/firstpage_need_png/img1.png') no-repeat center;
        background-size: cover;
        width:280px;
        height:420px;
        top:-90px;
        right:-400px;
    }
    .img2{
        position:absolute;
        background:url('../../assets/firstpage_need_png/img2.png') no-repeat center;
        background-size: cover;
        width:300px;
        height:200px;
        top:230px;
        right:-150px;
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

  },
  methods:{
      left(){
          if(this.present>1) {
              this.present -= 1;
          }
          else
          {
              this.present=1
          }

      },
      right(){
          if(this.present<4)
          {
              this.present+=1;
          }
          else
          {
              this.present=4;
          }
      },
      clickk(val){
        alert(val);
          location.replace('/details')



        // this.$axios.post('http://127.0.0.1:5000/api/first',val)
      },
      Time(){
          //倒计时

          setInterval(()=>{let now = new Date();
        let future = new Date("2029-11-8 8:00:45");
        let offset = Math.floor((future.getTime()-now.getTime())/1000);
        // 天

        // 小时
        let hourNum = Math.floor(offset/(60*60));
        this.hour = hourNum;
        // 分钟
        let minNum = Math.floor((offset)%(60*60)/60);
        this.minute = minNum;
        // 秒
        let secNum = Math.floor(offset%(60*60)%60);
        this.sec = secNum;
        },1000);


      },

  },
    created(){
       this.Time();
    },
  data(){
    return{
    hour:'',
    minute:'',
    sec:'',
    present:1,
    lines:[
        {
            source:'HENRIKSDAL 亨利克',
            descript:'椅子，桦木，格雷伯',
            price:'499',
        },
        {
            source:'PROANG-波昂',
            descript:'沙发套可拆洗',
            price:'999.00',
        },
        {
            //第四行的左边的数据
            source:'索 德 汉',
            descript:'脚凳，芬斯塔 天蓝色',
            price:'349.00',
        },
        {
            //第四行的右边的数据
            source:'安 迪 福',
            descript:'落地灯/阅读灯，镀镍',
            price:'299.00',
        },
        {
            source:'STRANDMON 斯 佳 蒙',
            descript:'背靠椅 ，尤帕 深绿色',
            price:'499.00',
        },
    ],
     //   横向商品
     rows:[
            {
            source:'维 哈 默',
            price:'299.00',
        },
          {
            source:'马 克 鲁 斯',
            price:'199.00',
        },
         {
            source:'哈 马 恩',
            price:'399.00',
        },
            {
            source:'奥 恩 迪',
            price:'99.00',
        },
        ]
    }
  },
}
</script>
