<template>
    <div class="one-box">
        <template>
            <el-table :data="tableData" style="width: 100%" max-height="1000" :header-cell-style='tableHeaderStyle'>
                <el-table-column type="selection" width="55"></el-table-column>
                <el-table-column prop="qx" label="全选" width="160"></el-table-column>
                <el-table-column prop="spms" label="商品描述" width="140"></el-table-column>
                <el-table-column prop="sl" label="数量" width="140"></el-table-column>
                <el-table-column prop="dj" label="单价" width="140"></el-table-column>
                <el-table-column prop="zt1" label="状态" width="140"></el-table-column>
                <el-table-column prop="zt2" label="状态" width="120">
                    <el-button type="info">
                        查看物流
                    </el-button>
                </el-table-column>
            </el-table>
        </template>
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
                tableData: [{
                    qx: '2016-05-03',
                    spms: 'POANG-波昂',
                    sl: '1',
                    dj: '699.00RMB',
                    zt1: '待发货'
                }, ],
                tableHeaderStyle:{

                }
            }
        }
    }
</script>
<style scoped>


    .el-button{
        width: 60px!important;
        padding: 5px!important;
        font-size: 12px;
    }
</style>