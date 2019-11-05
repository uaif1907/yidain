<template>
    <div class="paid-box">
        <el-row :span="24">
            <div class="size">
                <span></span>
                <h4>无效订单</h4>
                <span></span>
            </div>
            <el-table :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase())).slice((currentPage-1)*pageSize,currentPage*pageSize)" style="width: 100%">
                <el-table-column label="#" prop="id" width="50"></el-table-column>
                <el-table-column label="订单号" prop="order" width="200"></el-table-column>
                <el-table-column label="消费者" prop="consumer" width="80"></el-table-column>
                <el-table-column label="联系方式" prop="phone" width="120"></el-table-column>
                <el-table-column label="地区" prop="area"></el-table-column>
                <el-table-column label="消费金额" prop="monetary"></el-table-column>
                <el-table-column label="支付方式" prop="pay">
                    <template slot-scope="scope">
                        <Status :status="scope.row.pay"></Status>
                    </template>
                </el-table-column>
                <el-table-column label="状态" prop="state">
                    <template slot-scope="scope">
                        <Status :status="scope.row.state"></Status>
                    </template>
                </el-table-column>
                <el-table-column label="下单时间" prop="ordertime" width="150"></el-table-column>
                <el-table-column align="right" label="操作">
                    <template slot-scope="scope">
                        <el-button size="mini" style="background: -webkit-linear-gradient(left,#67c1fd,#71dcfd);color: white" @click="handleDelete(scope.row)">查看详情</el-button>
                    </template>
                </el-table-column>
            </el-table>

        </el-row>
<!--        分页-->
        <div class="block">
                        <el-pagination
                                @size-change="handleSizeChange"
                                @current-change="handleCurrentChange"
                                :current-page.sync="currentPage"
                                :page-sizes="[10, 20, 30, 40]"
                                :page-size="pageSize"
                                layout="sizes, prev, pager, next"
                                :total="total"
                                background>
                        </el-pagination>
                    </div>
    </div>
</template>

<script>
    import Status from '@/components/data/status.vue'
    export default {
        name: 'Paid',
        props: {
            // msg: String
        },
        data(){
            return {
                total:100,
                currentPage:1,
                pageSize:9,
                tableData: [{
                    id:1,
                    order:'524FRG27483676',
                    consumer:'张三',
                    phone:123876798003,
                    area:'北京朝阳',
                    monetary:"￥4233.00",
                    pay:0,
                    state:6,
                    ordertime:'2019-05-25 9:00',
                }, {
                    id:2,
                    order:'524FRG27483677',
                    consumer:'李四',
                    phone:123876798003,
                    area:'北京朝阳',
                    monetary:"￥4233.00",
                    pay:1,
                    state:9,
                    ordertime:'2019-05-25 9:00',
                }, {
                    id:3,
                    order:'524FRG27483678',
                    consumer:'王五',
                    phone:123876798003,
                    area:'北京朝阳',
                    monetary:"￥4233.00",
                    pay:4,
                    state:10,
                    ordertime:'2019-05-25 9:00',
                }, {
                    id:4,
                    order:'524FRG27483679',
                    consumer:'马六',
                    phone:123876798003,
                    area:'北京朝阳',
                    monetary:"￥4233.00",
                    pay:1,
                    state:6,
                    ordertime:'2019-05-25 9:00',
                },
                {
                    id:5,
                    order:'524FRG27483676',
                    consumer:'张三',
                    phone:123876798003,
                    area:'北京朝阳',
                    monetary:"￥4233.00",
                    pay:0,
                    state:6,
                    ordertime:'2019-05-25 9:00',
                }, {
                    id:6,
                    order:'524FRG27483677',
                    consumer:'李四',
                    phone:123876798003,
                    area:'北京朝阳',
                    monetary:"￥4233.00",
                    pay:1,
                    state:9,
                    ordertime:'2019-05-25 9:00',
                }, {
                    id:7,
                    order:'524FRG27483678',
                    consumer:'王五',
                    phone:123876798003,
                    area:'北京朝阳',
                    monetary:"￥4233.00",
                    pay:4,
                    state:10,
                    ordertime:'2019-05-25 9:00',
                }, {
                    id:8,
                    order:'524FRG27483679',
                    consumer:'马六',
                    phone:123876798003,
                    area:'北京朝阳',
                    monetary:"￥4233.00",
                    pay:1,
                    state:6,
                    ordertime:'2019-05-25 9:00',
                },
                {
                    id:9,
                    order:'524FRG27483676',
                    consumer:'张三',
                    phone:123876798003,
                    area:'北京朝阳',
                    monetary:"￥4233.00",
                    pay:0,
                    state:6,
                    ordertime:'2019-05-25 9:00',
                }, {
                    id:10,
                    order:'524FRG27483677',
                    consumer:'李四',
                    phone:123876798003,
                    area:'北京朝阳',
                    monetary:"￥4233.00",
                    pay:1,
                    state:9,
                    ordertime:'2019-05-25 9:00',
                }, {
                    id:11,
                    order:'524FRG27483678',
                    consumer:'王五',
                    phone:123876798003,
                    area:'北京朝阳',
                    monetary:"￥4233.00",
                    pay:4,
                    state:10,
                    ordertime:'2019-05-25 9:00',
                }, {
                    id:12,
                    order:'524FRG27483679',
                    consumer:'马六',
                    phone:123876798003,
                    area:'北京朝阳',
                    monetary:"￥4233.00",
                    pay:1,
                    state:6,
                    ordertime:'2019-05-25 9:00',
                }],
            }
        },
        methods: {
            handleSelect() {
            },
            handleClose() {
            },
            handleSizeChange() {
                // console.log(`每页 ${val} 条`);
            },
            handleCurrentChange(val) {
                // console.log(`当前页: ${val}`);
                this.currentPage = val;
            }
        },
        components:{
            Status
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.size{
        position: relative;
        /*left: 12px;*/
        /*top: 30px;*/
        /*display: inline-block;*/
        float: left;
        display: flex;
        width: 100%;
        margin: 15px;
    }
    .size h4{
        margin: 0 5px;
        font-weight: 400;
    }
    .size span{
        width: 16px;
        height: 3px;
        background: -webkit-linear-gradient(left,#67c1fd,#71dcfd);
        border-radius: 2px;
        margin-top: 10px;
    }

</style>
