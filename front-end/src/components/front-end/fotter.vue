<template>
  <div class="fotter-box" style="width: 1200px;margin: 0 auto;background: white;border-top:2px solid #e5e5e5">
      <el-row :span="24">
          <el-col :span="10" class="fotte-col" >
              <div><img src="../../assets/fotte/图层19拷贝3.png" alt="" style="padding-bottom: 80px;"><p style="font-weight: 600;font-size: 14px">官方微信</p></div>
              <div ><img src="../../assets/fotte/图层18拷贝3.png" alt="" style="padding-bottom: 74px;"><p style="font-weight: 600 ;font-size: 14px">小程序</p></div>
              <div style="margin-top: 80px;"><img src="../../assets/fotte/图层17拷贝3.png" alt="" ><p style="padding-bottom:76px;font-size: 12px;font-weight: 600">官方服务热线</p><p style="font-weight: 600 ;font-size: 14px">400-000-000</p></div>
          </el-col>
          <el-col :span="14">
                <div style="display: flex;text-align: center;line-height: 30px;padding-left: 50px">
                    <div style="width: 200px;height: 140px;line-height: 30px;padding-top:70px ">
                        <div style="font-weight: 600">售后保障</div>
                        <div style="font-size: 12px">物流配送</div>
                        <div style="font-size: 12px">收货指南</div>
                    </div>
                    <div style="width: 200px;height: 150px;line-height: 30px;padding-top:70px">
                        <div style="font-weight: 600">购物无忧</div>
                        <div style="font-size: 12px">品质保证</div>
                        <div style="font-size: 12px">保养说明</div>
                    </div>
                    <div style="width: 200px;height: 150px;line-height: 30px;padding-top:70px">
                        <div style="font-weight: 600">特色服务</div>
                        <div style="font-size: 12px">自由定制</div>
                    </div>
                </div>
                <div >
                    <el-row>
                        <el-col :span="12"><span style="font-size:12px;line-height: 30px">© Inter A LTTLE LIFE Systems B.V.1999 - 2019</span></el-col>
                        <el-col :span="12">
                            <el-input placeholder="Search for what you want"  class="input-with-select">
                                <el-button slot="append" icon="el-icon-search"></el-button>
                            </el-input>
                        </el-col>
                    </el-row>


                </div>
          </el-col>
      </el-row>
  </div>
</template>
<style scoped>
    .fotte-col{
        display: flex;
        justify-content: space-around;
    }
    .fotte-col>div{
        width: 100px;
        height: 200px;

        margin-top: 70px;
    }
</style>
<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'fotter',
  components: {
    // HelloWorld
  }
}
</script>
