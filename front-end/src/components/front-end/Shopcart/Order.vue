<template>
    <div>
        <el-table ref="multipleTable" align-center :data="tableData" tooltip-effect="dark" style="width: 100%;margin-top:20px" @selection-change="handleSelectionChange">
      <el-table-column type="selection" width="80" label="全选"></el-table-column>
      <el-table-column label="商品描述" width="400" prop="describe"></el-table-column>
      <el-table-column prop="color" label="颜色" width="120"></el-table-column>
      <el-table-column prop="size" label="尺码" width="120"></el-table-column>
      <el-table-column prop="sun" label="数量" width="120"></el-table-column>
      <el-table-column prop="price" label="单价" width="120"></el-table-column>
      <el-table-column prop="total_price" label="总价" width="120"></el-table-column>
        </el-table>
    </div>
</template>
<script>
export default {
    name:'shopping',
    component:{
        
    }
}
</script>