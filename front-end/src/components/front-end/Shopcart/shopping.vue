<template>
    <div>
        <el-table ref="multipleTable"  :data="tableData" tooltip-effect="dark" style="width: 1200px;margin-top:20px" @selection-change="handleSelectionChange">
            <el-table-column type="selection" align="center" width="80" label="全选"></el-table-column>
            <el-table-column align="center" label="商品图片" width="250" prop='img'>
                <div class="block">
                    
                    <el-image :src="img"></el-image>
                </div>
            </el-table-column>
            <el-table-column label="商品描述" prop="describe" align="center" width="130">
                <!-- <el-row v-model="describe" style="background-color:blue;height:30px;"></el-row>
                <el-row v-model="color" style="background-color:red;height:30px;"></el-row> -->
            </el-table-column>
            <el-table-column prop="color" align="center" label="颜色" width="130"></el-table-column>
            <el-table-column prop="size" align="center" label="尺码" width="130"></el-table-column>
            <el-table-column prop="num" align="center" label="数量" width="130">
                <el-input-number v-model="num1" style="width:100px;" size="mini"></el-input-number>
            </el-table-column>
            <el-table-column prop="price" align="center" label="单价" width="120"></el-table-column>
            <el-table-column prop="total_price" align="center" label="总价" width="150"></el-table-column>
            <el-table-column>
                <el-button type="text" size="small" class="el-icon-delete">删除</el-button>
            </el-table-column>
                
        
        </el-table>
        <div style="width:1200px;height:100px;">
            <div style="float:left;font-size:12px;padding:50px 0 0 15px;">3个结果</div>
            <div style="float:right;padding:50px 0 0 15px;font-size:40px;color:red">
                {{monkey}}<font size=2 color=black>RMB</font>

            </div>
            <div style="float:right;font-size:12px;padding:50px 0 0 15px;">
                <p style="font-size:16px;">应付金额:</p>
                <p>Total payable</p>
            </div>
            <div style="float:right;font-size:16px;padding:50px 50px 0 15px;">运费：<font size=6>300.00</font><font size=2>RMB</font></div>
        </div>
        
    </div>
</template>
<script>
export default {
    name:'shopping',
    component:{
        
    },
    data() {
      return {
          monkey:3146.00,
        // describe:'POANG-波昂'+'\n'+'有效',
        // color:"红色",
        num1:1,
        img:'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg',
        tableData:[
          {
            
            describe:['POANG-波昂'+'\n'+'摇椅 北欧风'],
            color:"桦木贴面，基尼萨淡米色",
            size:['W:59cm'+ '\n'+"H:23cm"+ '\n'+"L:87cm"],
            num:'1',
            price:'13451￥',
            total_price:'13451￥'

            
          },
        ],
        multipleSelection: []
      };
    },
    methods: {
    //     handleClick(row) {
    //     // console.log(row);
    //   },
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
    .el-input-number__increase{
        border-radius: 50%;
        background-color: aqua;
    }
    .el-table .cell {
            /* word-wrap: break-word; */
            text-align: center;
            white-space: pre-line;/*保留换行符*/
        }
</style>