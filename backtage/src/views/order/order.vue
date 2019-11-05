<template>
    <div class="header-box">
        <!--        <router-view></router-view>-->
        <el-row :span="24" style="background-color: #ffffff">
            <div class="size">
                <span></span>
                <h4>订单查询</h4>
                <span></span>
            </div>
            <el-form ref="form" :model="form" label-width="80px">
                <el-row>
                    <el-col :span="6">
                        <el-form-item label="订单号">
                            <el-input v-model="form.name" size="small" placeholder="请输入订单号"></el-input>
                        </el-form-item>
                    </el-col>
                    <el-col :span="6">
                        <el-form-item label="消费者">
                            <el-input v-model="form.consumer" size="small" placeholder="请输入名字"></el-input>
                        </el-form-item>
                    </el-col>
                    <el-col :span="6">
                        <el-form-item label="手机号">
                            <el-input v-model="form.phone" size="small" placeholder="请输入手机号"></el-input>
                        </el-form-item>
                    </el-col>
                    <el-col :span="6">
                        <el-form-item label="支付方式">
                            <el-select v-model="form.pay" placeholder="支付方式" size="small">
                                <el-option label="微信" value="微信"></el-option>
                                <el-option label="支付宝" value="支付宝"></el-option>
                                <el-option label="银联" value="银联"></el-option>
                            </el-select>
                        </el-form-item>
                    </el-col>
                    <el-col :span="6">
                        <el-form-item label="地区">
                            <el-input v-model="form.area" size="small" placeholder="省/市/县"></el-input>
                        </el-form-item>
                    </el-col>
                    <el-col :span="6" style="margin-right: 100px">
                        <el-form-item label="状态">
                            <el-select v-model="form.state" placeholder="请选择" size="small" style="width: 220px">
                                <el-option label="待收货" value="待收货"></el-option>
                                <el-option label="待配货" value="待配货"></el-option>
                                <el-option label="已完成" value="已完成"></el-option>
                            </el-select>
                        </el-form-item>
                    </el-col>
                    <el-col :span="13">
                        <el-form-item label="下单时间">
                            <el-time-select
                                    placeholder="起始时间"
                                    v-model="form.startTime"
                                    size="small"
                                    style="float: left"
                                    :picker-options="{
                                      start: '08:30',
                                      step: '00:15',
                                      end: '18:30',
                                    }">
                            </el-time-select>
                            <el-time-select
                                    placeholder="结束时间"
                                    v-model="form.ordertime"
                                    size="small"
                                    style="margin-left: 74px"
                                    :picker-options="{
                                      start: '08:30',
                                      step: '00:15',
                                      end: '18:30',
                                      minTime: startTime
                                    }">
                            </el-time-select>
                        </el-form-item>
                    </el-col>
                    <el-col :span="2" class="cx-box">
                        <el-button type="primary" size="small" class="cx-bottom" @click="handleSelect()">查询</el-button>
                    </el-col>
                </el-row>
            </el-form>
        </el-row>
        <!--进度条-->
        <el-row :span="24" style="background-color: #ffffff;margin: 20px 0;padding-bottom: 20px;">
            <div class="size">
                <span></span>
                <h4>订单详情</h4>
                <span></span>
                <el-row :span="8" style="position:absolute;right:0;margin-bottom: 20px">
                <el-col :span="4" style="width: 100px;margin-right: 20px;">
                    <el-select v-model="form.dq" placeholder="地区" size="small">
                        <el-option label="北京" value="北京"></el-option>
                        <el-option label="上海" value="上海"></el-option>
                        <el-option label="广州" value="广州"></el-option>
                    </el-select>
                </el-col>
                <el-col :span="4" style="width: 100px;float: right;">
                    <el-select v-model="form.zj" placeholder="最近" size="small">
                        <el-option label="最近7天" value="最近7天"></el-option>
                        <el-option label="最近30天" value="最近30天"></el-option>
                        <el-option label="最近半年" value="最近半年"></el-option>
                    </el-select>
                </el-col>
            </el-row>
            </div>

            <el-col :span="6" class="ding-box">
                <el-progress type="circle" :percentage="80" style="margin-left: 40px" :stroke-width="10" color="#72cbfc"></el-progress>
                <div class="zi">
                    <h3>已完成订单</h3>
                    <h4>452.00万</h4>
                    <h6>144314件</h6>
                </div>
            </el-col>
            <el-col :span="6" class="ding-box">
                <el-progress type="circle" :percentage="40" style="margin-left: 40px" :stroke-width="10" color="#d589e1"></el-progress>
                <div class="zi">
                    <h3>待收货订单</h3>
                    <h4 style="color: #d589e1">32.00万</h4>
                    <h6>144件</h6>
                </div>
            </el-col>
            <el-col :span="6" class="ding-box">
                <el-progress type="circle" :percentage="50" style="margin-left: 40px" :stroke-width="10" color="#f9ce7a"></el-progress>
                <div class="zi">
                    <h3>待配送订单</h3>
                    <h4 style="color: #f9ce7a">43.00万</h4>
                    <h6>146件</h6>
                </div>
            </el-col>
            <el-col :span="6" class="ding-box">
                <el-progress type="circle" :percentage="80" style="margin-left: 40px" :stroke-width="10" color="#45e18f"></el-progress>
                <div class="zi">
                    <h3>未评论订单</h3>
                    <h4 style="color: #45e18f">452.00万</h4>
                    <h6>144314件</h6>
                </div>
            </el-col>
        </el-row>
        <!--表单-->
        <el-row :span="24">
            <div class="size">
                <span></span>
                <h4>订单列表</h4>
                <span></span>
            </div>
            <el-table :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))" style="width: 100%">
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

        <!--查看详情-->
        <el-dialog title="查看详情" :visible.sync="dialogFormVisible" width="70%">
            <el-form :model="formDate">
                <el-row :span="24" style="display: flex;justify-content: space-between">
                    <el-col :span="6">
                        <el-form-item label="订单号">
                            <el-input v-model="formDate.order" size="small" placeholder="请输入订单号" class="add" disabled></el-input>
                        </el-form-item>
                    </el-col>
                    <el-col :span="6">
                        <el-form-item label="消费者">
                            <el-input v-model="formDate.consumer" size="small" placeholder="请输入订单号" class="add" disabled></el-input>
                        </el-form-item>
                    </el-col>
                    <el-col :span="6">
                        <el-form-item label="联系方式">
                            <el-input v-model="formDate.phone" size="small" placeholder="请输入订单号" class="add" disabled></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row :span="24" style="display: flex;justify-content: space-between">
                    <el-col :span="6">
                        <el-form-item label="地区">
                            <el-input v-model="formDate.area" size="small" placeholder="请输入订单号" class="add" disabled></el-input>
                        </el-form-item>
                    </el-col>
                    <el-col :span="6">
                        <el-form-item label="消费金额">
                            <el-input v-model="formDate.monetary" size="small" placeholder="请输入消费金额" class="add" disabled></el-input>
                        </el-form-item>
                    </el-col>
                    <el-col :span="6">
                        <el-form-item label="支付方式">
                            <el-input v-model="formDate.pay" size="small" placeholder="支付方式" class="add" disabled></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row :span="24" style="display: flex;justify-content: space-between">
                    <el-col :span="6">
                        <el-form-item label="状态">
                            <el-input v-model="formDate.state" size="small" placeholder="状态" class="add" disabled></el-input>
                        </el-form-item>
                    </el-col>
                    <el-col :span="6">
                        <el-form-item label="下单时间">
                            <el-input v-model="formDate.ordertime" size="small" placeholder="下单时间" class="add" disabled></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="dialogFormVisible = false">取 消</el-button>
                <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
            </div>
        </el-dialog>
        <!--查询-->
        <el-dialog title="查看详情" :visible.sync="dialogFormtable" width="70%">
            <el-form :model="adddata">
                <el-row :span="24" style="display: flex;justify-content: space-between">
                    <el-col :span="6">
                        <el-form-item label="订单号">
                            <el-input v-model="adddata.order" size="small" placeholder="请输入订单号" class="add" disabled></el-input>
                        </el-form-item>
                    </el-col>
                    <el-col :span="6">
                        <el-form-item label="消费者">
                            <el-input v-model="adddata.consumer" size="small" placeholder="请输入订单号" class="add" disabled></el-input>
                        </el-form-item>
                    </el-col>
                    <el-col :span="6">
                        <el-form-item label="联系方式">
                            <el-input v-model="adddata.phone" size="small" placeholder="请输入订单号" class="add" disabled></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row :span="24" style="display: flex;justify-content: space-between">
                    <el-col :span="6">
                        <el-form-item label="地区">
                            <el-input v-model="adddata.area" size="small" placeholder="请输入订单号" class="add" disabled></el-input>
                        </el-form-item>
                    </el-col>
                    <el-col :span="6">
                        <el-form-item label="消费金额">
                            <el-input v-model="adddata.monetary" size="small" placeholder="请输入消费金额" class="add" disabled></el-input>
                        </el-form-item>
                    </el-col>
                    <el-col :span="6">
                        <el-form-item label="支付方式">
                            <el-input v-model="adddata.pay" size="small" placeholder="支付方式" class="add" disabled></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
                <el-row :span="24" style="display: flex;justify-content: space-between">
                    <el-col :span="6">
                        <el-form-item label="状态">
                            <el-input v-model="adddata.state" size="small" placeholder="状态" class="add" disabled></el-input>
                        </el-form-item>
                    </el-col>
                    <el-col :span="6">
                        <el-form-item label="下单时间">
                            <el-input v-model="adddata.ordertime" size="small" placeholder="下单时间" class="add" disabled></el-input>
                        </el-form-item>
                    </el-col>
                </el-row>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="dialogFormtable = false">取 消</el-button>
                <el-button type="primary" @click="dialogFormtable = false">确 定</el-button>
            </div>
        </el-dialog>
    </div>
</template>

<script>
    import Status from '@/components/data/status.vue'
    export default {
        name: 'Header',
        props: {
            // msg: String
        },
        data(){
            return {
                adddata:{monetary:"￥4233.00"},
                dialogFormtable:false,
                dialogFormVisible: false,
                formLabelWidth: '120px',
                formDate:{},
                form: {
                    name: '',
                    region: '',
                    date1: '',
                    date2: '',
                    delivery: false,
                    type: [],
                    resource: '',
                    desc: '',

                },
                startTime: '',
                endTime: '',
                search: '',
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
                }],
            }
        },
        methods: {
            handleSelect() {
                this.dialogFormtable=true
                this.adddata=this.form
            },
            handleClose() {
            },
            handleDelete(row) {
                // alert(index, row);this.showDialogTableVisible = true;
                this.formDate = row;
                this.dialogFormVisible = true
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
    .cx-box{
        margin-top: 5px;
    }
    .cx-bottom{
        width: 100px;
        border: none!important;
        background: -webkit-linear-gradient(left,#67c1fd,#71dcfd)!important;
    }
    .ding-box{
        display: flex;
    }
    .zi{
        display: flex;
        flex-direction: column;
        justify-content: center;
        margin-left: 30px;
        text-align: left;
    }
    .zi h3{
        font-weight: 400;
        color: #666666;
    }
    .zi h4{
        font-weight: 400;
        color: #8dc1e4;
    }
    .zi h6{
        color: #9f9f9f;
    }

</style>
