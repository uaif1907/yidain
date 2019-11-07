<template>
    <div class="pay">
        <el-row>
           <div style="width: 1200px;height: 400px">
                <div style="text-align: left;padding: 100px 10px;padding-bottom: 0;position: relative;">
                    <img src="../../../assets/shopcart/图层46拷贝2.png" alt="" style="float: left">
                    <div style="width: 2px;height: 20px;background:#ccc;border-radius: 10px;float: left;margin-top: 5px;margin-left: 5px"></div>
                    <div style="float: left;margin-left: 10px">
                        <p style="font-weight: 600;font-size: 16px">配送地址</p>
                        <p style="font-size:9px;color: #9f9f9f">SHIPPING ADDRESS</p>
                    </div>
                    <div style="width: 67px;height:67px;background-color: #5ed5e0;color: white;opacity: 0.9;border-radius: 100%;text-align:center;font-size:30px;line-height:70px;position:absolute;left: 95px;top:65px;z-index: -1"><span style="opacity: 0.7">01</span></div>
                </div>
               <el-row style="margin-top: 50px;margin-left: 15px">
                   <div class="order-address">
                    <div class="order-address1">
                        <el-row>
                            <div style="float: right;font-size: 18px;color:#b4b4b4 ;">
                                <i class="el-icon-edit-outline" style="margin-right: 30px"></i>
                                <i class="el-icon-delete"></i>
                            </div>
                        </el-row>
                        <el-row>
                            <div style="font-weight: 600;font-size: 18px;text-align:left">李 思 思</div>
                        </el-row>
                        <el-row>
                            <div style="font-size: 18px;text-align:left;margin-top: 20px;color:#b4b4b4">
                                <i class="el-icon-mobile" style="margin-right: 20px"></i>
                                <span style="font-size: 14px;color: black;">19793764747</span>
                            </div>
                        </el-row>
                        <el-row>
                            <div style="font-size: 18px;text-align:left;margin-top: 20px;margin-bottom:10px;color:#b4b4b4">
                                <i class="el-icon-location-outline" style="margin-right: 20px"></i>
                                <span style="font-size: 14px;color: black;">北京市 北京市 西城区 西长安街街道</span>
                            </div>
                        </el-row>
                        <el-row style="float: right">
                             <el-button type="info" size="small" >默认</el-button>
                        </el-row>
                    </div>


                 </div>
                       <div class="order-add"   @click="dialogFormVisible = true">
                            <i  class="el-icon-plus avatar-uploader-icon ">
                                <p style="font-size: 16px;">添加收货地址</p>
                            </i>
                       </div>

<!--                           弹出-->
                           <el-dialog title="· 收货地址 ·" :visible.sync="dialogFormVisible" width="40%">
                              <el-form :model="form" :inline="true">
                                <el-form-item label="姓名" :label-width="formLabelWidth">
                                  <el-input v-model="orderform.name" autocomplete="off" style="width: 460px"></el-input>
                                </el-form-item>
                                  <el-form-item label="电话" :label-width="formLabelWidth">
                                  <el-input v-model="orderform.tel" autocomplete="off" style="width: 460px"></el-input>
                                </el-form-item>
                                  <el-row>
                                      <el-form-item label="省" :label-width="formLabelWidth" >
                                  <el-select v-model="orderform.region" style="width: 90px">
                                    <el-option label="区域一" value="shanghai"></el-option>
                                    <el-option label="区域二" value="beijing"></el-option>
                                  </el-select>
                                </el-form-item>
                                      <el-form-item label="市" :label-width="formLabelWidth">
                                  <el-select v-model="orderform.region" style="width: 90px">
                                    <el-option label="区域一" value="shanghai"></el-option>
                                    <el-option label="区域二" value="beijing"></el-option>
                                  </el-select>
                                </el-form-item>
                                      <el-form-item label="区" :label-width="formLabelWidth">
                                  <el-select v-model="orderform.region" style="width: 90px">
                                    <el-option label="区域一" value="shanghai"></el-option>
                                    <el-option label="区域二" value="beijing"></el-option>
                                  </el-select>
                                </el-form-item>
                                  </el-row>
                                <el-form-item label="街道地址" label-width="80px">
                                  <el-select v-model="orderform.region" style="width: 460px">
                                    <el-option label="区域一" value="shanghai"></el-option>
                                    <el-option label="区域二" value="beijing"></el-option>
                                  </el-select>
                                </el-form-item>
                              </el-form>

                              <div slot="footer" class="dialog-footer" style="margin: 0 auto">
                                  <el-button type="info" @click="dialogVisible = false">保存</el-button>
                                <el-button type="info" plain @click="dialogVisible = false">取 消</el-button>

                              </div>
                            </el-dialog>
<!--                           弹出结束-->
               </el-row>


           </div>
        </el-row>
        <el-row>
            <div style="width: 1200px;height: 400px">
                <div style="text-align: left;padding: 100px 10px;padding-bottom: 0;position: relative;">
                    <img src="../../../assets/shopcart/图层46拷贝2.png" alt="" style="float: left">
                    <div style="width: 2px;height: 20px;background:#ccc;border-radius: 10px;float: left;margin-top: 5px;margin-left: 5px"></div>
                    <div style="float: left;margin-left: 10px">
                        <p style="font-weight: 600;font-size: 16px">商品信息</p>
                        <p style="font-size:9px;color: #9f9f9f">PRODUCTINFO</p>
                    </div>
                    <div style="width: 67px;height:67px;background-color: #5ed5e0;color: white;opacity: 0.9;border-radius: 100%;text-align:center;font-size:30px;line-height:70px;position:absolute;left: 95px;top:65px;z-index: -1"><span style="opacity: 0.7">02</span></div>
                </div>


            </div>
        </el-row>
    </div>
</template>
<style scoped>
    .order-address{
        width: 400px;
        height: 190px;
        border: 2px solid #b2b2b2;
        padding: 10px;
        float: left;
        margin-right: 60px;
    }
    .order-address1{
        border: 2px dashed #e5e5e5;
        height: 166px;
        padding: 10px;
        padding-left: 20px;
    }
    .order-add{
        width: 210px;
        height: 210px;
        border: 2px solid #e5e5e5;
        float: left;
        line-height: 240px;
        font-size: 50px;
        color: #d0d0d0;
    }
</style>
<script>
export default {
    name:'shopping',
    data() {
      return {
        dialogFormVisible: false,
          orderform: {
          name: '',
              tel:'',
          region: '',
          date1: '',
          date2: '',
          delivery: false,
          type: [],
          resource: '',
          desc: ''
        },
          formLabelWidth: '80px',
      };
    },
    component:{
        
    }
}
</script>