<template>
  <div class="home">
    <!-- 面包屑 -->
    
    <el-breadcrumb separator="/" style="width:100%;height:50px;line-height:50px;">
      <div class="yuan"></div>
      <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item><a href="/">购物车</a></el-breadcrumb-item>
    </el-breadcrumb>
    
    
    <!-- 步骤条 -->
    <div class="Step">
      <el-steps :active="active" align-center>
        <el-step title="查看购物车"></el-step>
        <el-step title="填写订单信息"></el-step>
        <el-step title="选择支付方式"></el-step>
        <el-step title="成功提交订单"></el-step>
      </el-steps>
    </div>
    
    
    
    <!-- 列表 -->
    <el-table ref="multipleTable" align-center :data="tableData" tooltip-effect="dark" style="width: 100%;margin-top:20px" @selection-change="handleSelectionChange">
      <el-table-column type="selection" width="80" label="全选"></el-table-column>
      <el-table-column label="商品描述" width="400" prop="describe"></el-table-column>
      <el-table-column prop="color" label="颜色" width="120"></el-table-column>
      <el-table-column prop="size" label="尺码" width="120"></el-table-column>
      <el-table-column prop="sun" label="数量" width="120"></el-table-column>
      <el-table-column prop="price" label="单价" width="120"></el-table-column>
      <el-table-column prop="total_price" label="总价" width="120"></el-table-column>
      
    </el-table>

    <el-button style="margin-top: 12px;" @click="next">结算</el-button>
    
  </div>
  
</template>

<script>
// @ is an alias to /src


export default {
  name: 'ShopCar',
  components: {

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

.Step{
  padding-top: 20px;
  width: 100%;
  height: 80px;
  background-color: #f3f3f3;
}
</style>