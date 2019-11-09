<template>
    <div class="one-box">
        <el-table :data="tableData" tooltip-effect="dark" style="width: 100%" max-height="1000">
            <el-table-column type="selection" align="center" width="55"></el-table-column>
            <el-table-column prop="img" align="center" label="商品图片" width="160">
                <template slot-scope="scope">
                    <img :src="scope.row.img" alt="">
                </template>
            </el-table-column>
            <el-table-column align="center" label="商品描述" width="140">
                <template slot-scope="scope">
                    <p style=""><strong>{{ scope.row.name }}</strong></p>
                    <p>{{ scope.row.describe }}</p>
                </template>
            </el-table-column>
            <el-table-column prop="sl" align="center" label="数量" width="140">

            </el-table-column>
            <el-table-column prop="dj" align="center" label="单价" width="140">

            </el-table-column>
            <el-table-column prop="zt" align="center" label="状态" width="140">

            </el-table-column>
            <el-table-column align="center" label="物流" width="120">
                <el-button type="info">
                    查看物流
                </el-button>
            </el-table-column>
        </el-table>
    </div>
</template>
<script>
    export default {
        name: 'one-box',
        components: {
        },
        methods: {
            deleteRow(index, rows) {
                rows.splice(index, 1);
            }
        },
        data() {
            return {
                tableData: [
                    {
                        name:'POANG-波昂',
                        describe:'摇椅 北欧风',
                        sl: '1',
                        dj: '699.00RMB',
                        zt: '待发货',
                        img:require('../../../assets/person_img/图层85.png')
                    },
                    {
                        name:'ODGER-奥德格',
                        describe:'餐椅 北欧风',
                        sl: '1',
                        dj: '399.00RMB',
                        zt: '待发货',
                        img:require('../../../assets/person_img/图层87.png')
                    },
                    {
                        name:'ADE-阿德',
                        describe:'餐椅 简约风',
                        sl: '1',
                        dj: '456.00RMB',
                        zt: '待发货',
                        img:require('../../../assets/person_img/图层88.png')
                    },
                    {
                        name:'ANTILOP-安迪咯',
                        describe:'高脚椅 北欧风',
                        sl: '1',
                        dj: '467.00RMB',
                        zt: '待发货',
                        img:require('../../../assets/person_img/图层89.png')
                    },
                ],
                tableHeaderStyle:{

                }
            }
        }
    }
</script>
<style scoped>


    .el-button{
        width: 80px!important;
        padding: 8px!important;
        font-size: 12px;
    }
</style>