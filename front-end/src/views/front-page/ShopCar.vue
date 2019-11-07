<template>
  <div class="home">
    <!-- 面包屑 -->
    
    <el-breadcrumb separator="/" style="width:100%;height:50px;line-height:50px;">
      <div class="yuan"></div>
      <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item><a href="/">购物车</a></el-breadcrumb-item>
    </el-breadcrumb>
    
    
    <!-- 步骤条 -->
    
      <el-steps :active="active" align-center style="background-color:#f3f3f3;padding:20px 0;">
        <el-step title="查看购物车"></el-step>
        <el-step title="填写订单信息"></el-step>
        <el-step title="选择支付方式"></el-step>
        <el-step title="成功提交订单"></el-step>
      </el-steps>
      <div v-if="active===0">
        <Shopping></Shopping>
      </div>
      <div v-if="active===1">
        <Order></Order>
      </div>
      <div v-if="active===2">
        <Pay></Pay>
      </div>
      <div v-if="active===3">
        <Success></Success>
      </div>
    
    
    
    
    <!-- 列表 -->
    
      
    

    <el-button style="margin-top: 12px;background-color:#ccc;float:right;width:160px;height:60px;font-size:30px;color:white;" @click="next">结算</el-button>
    <Recommend></Recommend>
  </div>
  
</template>
<script>
// @ is an alias to /src
import Shopping from "@/components/front-end/Shopcart/shopping.vue"
import Order from "@/components/front-end/Shopcart/Order.vue"
import Pay from "@/components/front-end/Shopcart/Pay.vue"
import Success from "@/components/front-end/Shopcart/Success.vue"
import Recommend from "@/components/front-end/recommend/Recommend.vue"




export default {
  name: 'ShopCar',
  components: {
    Shopping,Order,Pay,Success,Recommend,
  },
  data() {
      return {
        active: 0,
        tableData:[
          {
            
          },
        ],
        multipleSelection: []
      };
    },

    methods: {
      next() {
        if (this.active++ > 2) this.active = 0;
      },
      toggleSelection(rows) {
        if (rows) {
          rows.forEach(row => {
            this.$refs.multipleTable.toggleRowSelection(row);
          });
        } else {
          this.$refs.multipleTable.clearSelection();
        }
      },
      handleSelectionChange(val) {
        this.multipleSelection = val;
      },
    }
}
</script>

<style scoped>
.yuan{
  float: left;
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background-color: #4cc0cb;
  margin-top: 20px;
  margin-right: 5px;
}

/* .el-step{
  padding-top: 20px;
  width: 100%;
  
  background-color: #f3f3f3;
} */
</style>