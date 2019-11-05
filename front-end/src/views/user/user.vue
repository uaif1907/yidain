<template>
    <div class="header-box">
        <!--        上面-->
        <el-row :span="24" style="display: flex;justify-content: space-between">
            <el-col :span="7" style="background-color: white">
                <div class="s-box">
                    <div class="size">
                        <span></span>
                        <h4>用户访问量</h4>
                        <span></span>
                    </div>
                    <div class="xz" @click="add=true">
                        <h6>最近6个月</h6>
                    </div>
                </div>
                <ve-radar :legend="legend" :radar="radar" :series="series" :colors="color"></ve-radar>
            </el-col>
            <el-col :span="8" style="background-color: white">
                <div class="size">
                    <span></span>
                    <h4>会员分布</h4>
                    <span></span>
                </div>
                <ve-ring :data="huanData" :settings="huanSettings" :legend="{bottom:10}" :extend="chartExtend"></ve-ring>
            </el-col>
            <el-col :span="8" style="background-color: white">
                <div class="size">
                    <span></span>
                    <h4>用户来源</h4>
                    <span></span>
                </div>
                <ve-ring :data="yhData" :settings="yhSettings" :legend="{bottom:10}" :extend="chartExtend"></ve-ring>
            </el-col>
        </el-row>
        <!--        表格-->
        <el-row :span="24">
            <div class="size">
                <span></span>
                <h4>订单列表</h4>
                <span></span>
            </div>
            <el-table :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))" style="width: 100%">
                <el-table-column label="#" prop="id" width="50"></el-table-column>
                <el-table-column label="身份证名" prop="order" width="200"></el-table-column>
                <el-table-column label="消费者" prop="consumer" width="80"></el-table-column>
                <el-table-column label="联系方式" prop="phone" width="120"></el-table-column>
                <el-table-column label="地区" prop="area"></el-table-column>
                <el-table-column label="消费金额" prop="monetary"></el-table-column>
                <el-table-column label="支付方式" prop="pay">
                    <template slot-scope="scope">
                        <Status :status="scope.row.pay"></Status>
                    </template>
                </el-table-column>
                <el-table-column label="来源" prop="state">
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
        <el-dialog title="用户资料" :visible.sync="dialogFormVisible" width="70%">
            <el-form :model="formDate">
                <el-row :span="24" style="display: flex;justify-content: space-between" class="xx-box">
                    <el-col :span="4">
                        <span>姓名</span>
                        <el-input v-model="formDate.consumer" size="small" placeholder="请输入姓名" class="add" disabled style="width: 160px;margin-top: 20px"></el-input>
                    </el-col>
                    <el-col :span="4">
                        <span>身份证</span>
                        <el-input v-model="formDate.order" size="small" placeholder="请输入身份证号" class="add" disabled style="width: 160px;margin-top: 20px"></el-input>
                    </el-col>
                    <el-col :span="4">
                        <span>手机号</span>
                        <el-input v-model="formDate.phone" size="small" placeholder="请输入手机号" class="add" disabled style="width: 160px;margin-top: 20px"></el-input>
                    </el-col>
                    <el-col :span="4">
                        <span>注册时间</span>
                        <el-input v-model="formDate.ordertime" size="small" placeholder="注册时间" class="add" disabled style="width: 160px;margin-top: 20px"></el-input>
                    </el-col>
                </el-row>
                <el-row :span="24" style="display: flex;justify-content: left;margin-top: 10px">
                    <el-col :span="4" style="margin:0  68px;">
                        <span>地区</span>
                        <el-input v-model="formDate.area" size="small" placeholder="地区" class="add" disabled style="width: 160px;margin-top: 20px"></el-input>
                    </el-col>
                    <el-col :span="4">
                        <span>总交易额</span>
                        <el-input v-model="formDate.monetary" size="small" placeholder="总交易额" class="add" disabled style="width: 160px;margin-top: 20px"></el-input>
                    </el-col>

                </el-row>
            </el-form>
            <el-row :span="24">
                <el-table :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase())).slice((currentPage-1)*pageSize,currentPage*pageSize)" style="width: 100%">
                    <el-table-column label="ID" prop="id" width="50"></el-table-column>
                    <el-table-column label="商品图片" width="200">
                        <el-image
                                style="width: 100px; height: 100px"
                                :src="url"
                                :preview-src-list="srcList"
                                prop="order">
                        </el-image>
                    </el-table-column>
                    <el-table-column label="金额" prop="monetary" width="100"></el-table-column>
                    <el-table-column label="支付方式" prop="pay">
                        <template slot-scope="scope">
                            <Status :status="scope.row.pay"></Status>
                        </template>
                    </el-table-column>
                    <el-table-column label="渠道" prop="area">
                        <template slot-scope="scope">
                            <Status :status="scope.row.state"></Status>
                        </template>
                    </el-table-column>
                    <el-table-column label="交易时间" prop="ordertime" width="140"></el-table-column>
                </el-table>
            </el-row>
            <div class="block">
                <el-pagination
                        :current-page.sync="currentPage"
                        :page-size="pageSize"
                        layout="prev, pager, next"
                        :total="4">
                </el-pagination>
            </div>
            <div slot="footer" class="dialog-footer">
                <el-button @click="dialogFormVisible = false">取 消</el-button>
                <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
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
            this.huanSettings = {
                dimension: '产品',
                metrics: '数量',
                radius: ['60px', '80px'],
                label: {
                    formatter: params => {
                        if (params.dataIndex === 0) {
                            return `{a| 西安${params.percent}%}`
                        } else if (params.dataIndex === 1){
                            return `{b| 北京${params.percent}%}`
                        } else if (params.dataIndex === 2){
                            return `{c| 杭州${params.percent}%}`
                        } else if (params.dataIndex === 3){
                            return `{d| 上海${params.percent}%}`
                        } else {
                            return `{e| 深圳${params.percent}%}`
                        }
                    },
                    rich: {
                        a: {color: '#ff4143'},
                        b: {color: '#f7c478'},
                        c: {color: '#cb79e6'},
                        d: {color: '#69c1fc'},
                        e: {color: '#47de8c'},
                    }
                },
                itemStyle: {
                    color: seriesIndex => {
                        if (seriesIndex.dataIndex === 0) {
                            return {
                                type: 'linear',
                                x: 0,
                                y: 1,
                                x2: 0,
                                y2: 0,
                                colorStops: [
                                    {
                                        offset: 0,
                                        color: '#ff4143' // 0% 处的颜色
                                    },
                                    {
                                        offset: 1,
                                        color: '#f86ba6' // 100% 处的颜色
                                    }
                                ],
                                global: false // 缺省为 false
                            };
                        }
                        else if (seriesIndex.dataIndex === 1){
                            return {
                                type: 'linear',
                                x: 0,
                                y: 1,
                                x2: 0,
                                y2: 0,
                                colorStops: [
                                    {
                                        offset: 0,
                                        color: '#f7c478' // 0% 处的颜色
                                    },

                                    {
                                        offset: 1,
                                        color: '#fde280' // 100% 处的颜色
                                    }
                                ],
                                global: false // 缺省为 false
                            };
                        }
                        else if (seriesIndex.dataIndex === 2){
                            return {
                                type: 'linear',
                                x: 0,
                                y: 1,
                                x2: 0,
                                y2: 0,
                                colorStops: [
                                    {
                                        offset: 0,
                                        color: '#cb79e6' // 0% 处的颜色
                                    },

                                    {
                                        offset: 1,
                                        color: '#faa2f9' // 100% 处的颜色
                                    }
                                ],
                                global: false // 缺省为 false
                            };
                        }
                        else if (seriesIndex.dataIndex === 3){
                            return {
                                type: 'linear',
                                x: 0,
                                y: 1,
                                x2: 0,
                                y2: 0,
                                colorStops: [
                                    {
                                        offset: 0,
                                        color: '#69c1fc' // 0% 处的颜色
                                    },

                                    {
                                        offset: 1,
                                        color: '#8eebfd' // 100% 处的颜色
                                    }
                                ],
                                global: false // 缺省为 false
                            };
                        }
                        else {
                            return {
                                type: 'linear',
                                x: 0,
                                y: 1,
                                x2: 0,
                                y2: 0,
                                colorStops: [
                                    {
                                        offset: 0,
                                        color: '#47de8c' // 0% 处的颜色
                                    },

                                    {
                                        offset: 1,
                                        color: '#24f5b2' // 100% 处的颜色
                                    }
                                ],
                                global: false // 缺省为 false
                            };
                        }
                    }
                }

            };
            this.chartExtend = {
                // legend: { show: false },
            };
            this.yhSettings = {
                dimension: '产品',
                metrics: '数量',
                radius: ['60px', '80px'],
                label: {
                    formatter: params => {
                        if (params.dataIndex === 0) {
                            return `{d| APP${params.percent}%}`
                        } else if (params.dataIndex === 1){
                            return `{b| WEB端${params.percent}%}`
                        } else if (params.dataIndex === 2){
                            return `{c| 移动端${params.percent}%}`
                        } else if (params.dataIndex === 3){
                            return `{d| 上海${params.percent}%}`
                        } else {
                            return `{e| 深圳${params.percent}%}`
                        }
                    },
                    rich: {
                        // a: {color: '#ff4143'},
                        b: {color: '#f7c478'},
                        c: {color: '#cb79e6'},
                        d: {color: '#69c1fc'},
                        // e: {color: '#47de8c'},
                    }
                },
                itemStyle: {
                    color: seriesIndex => {
                        if (seriesIndex.dataIndex === 0) {
                            return {
                                type: 'linear',
                                x: 0,
                                y: 1,
                                x2: 0,
                                y2: 0,
                                colorStops: [
                                    {
                                        offset: 0,
                                        color: '#69c1fc' // 0% 处的颜色
                                    },
                                    {
                                        offset: 1,
                                        color: '#8eebfd' // 100% 处的颜色
                                    }
                                ],
                                global: false // 缺省为 false
                            };
                        }
                        else if (seriesIndex.dataIndex === 1){
                            return {
                                type: 'linear',
                                x: 0,
                                y: 1,
                                x2: 0,
                                y2: 0,
                                colorStops: [
                                    {
                                        offset: 0,
                                        color: '#f7c478' // 0% 处的颜色
                                    },

                                    {
                                        offset: 1,
                                        color: '#fde280' // 100% 处的颜色
                                    }
                                ],
                                global: false // 缺省为 false
                            };
                        }
                        else if (seriesIndex.dataIndex === 2){
                            return {
                                type: 'linear',
                                x: 0,
                                y: 1,
                                x2: 0,
                                y2: 0,
                                colorStops: [
                                    {
                                        offset: 0,
                                        color: '#cb79e6' // 0% 处的颜色
                                    },

                                    {
                                        offset: 1,
                                        color: '#faa2f9' // 100% 处的颜色
                                    }
                                ],
                                global: false // 缺省为 false
                            };
                        }
                        else if (seriesIndex.dataIndex === 3){
                            return {
                                type: 'linear',
                                x: 0,
                                y: 1,
                                x2: 0,
                                y2: 0,
                                colorStops: [
                                    {
                                        offset: 0,
                                        color: '#69c1fc' // 0% 处的颜色
                                    },

                                    {
                                        offset: 1,
                                        color: '#8eebfd' // 100% 处的颜色
                                    }
                                ],
                                global: false // 缺省为 false
                            };
                        }
                        else {
                            return {
                                type: 'linear',
                                x: 0,
                                y: 1,
                                x2: 0,
                                y2: 0,
                                colorStops: [
                                    {
                                        offset: 0,
                                        color: '#47de8c' // 0% 处的颜色
                                    },

                                    {
                                        offset: 1,
                                        color: '#24f5b2' // 100% 处的颜色
                                    }
                                ],
                                global: false // 缺省为 false
                            };
                        }
                    }
                }

            };
            return {
                currentPage:1,
                pageSize:2,
                search:'',
                adddata:{monetary:"￥4233.00"},
                dialogFormtable:false,
                dialogFormVisible: false,
                formLabelWidth: '120px',
                formDate:{},
                tableData: [{
                    id:1,
                    order:'153427************',
                    consumer:'张三',
                    phone:123876798003,
                    area:'北京朝阳',
                    monetary:"￥4233.00",
                    pay:0,
                    state:12,
                    ordertime:'2019-05-25 9:00',
                },
                    {
                        id:2,
                        order:'153427************',
                        consumer:'李四',
                        phone:123876798003,
                        area:'北京朝阳',
                        monetary:"￥4233.00",
                        pay:1,
                        state:15,
                        ordertime:'2019-05-25 9:00',
                    },
                    {
                        id:3,
                        order:'153427************',
                        consumer:'王五',
                        phone:123876798003,
                        area:'北京朝阳',
                        monetary:"￥4233.00",
                        pay:4,
                        state:16,
                        ordertime:'2019-05-25 9:00',
                    },
                    {
                        id:4,
                        order:'153427************',
                        consumer:'马六',
                        phone:123876798003,
                        area:'北京朝阳',
                        monetary:"￥4233.00",
                        pay:1,
                        state:15,
                        ordertime:'2019-05-25 9:00',
                    }],
                color:['#d07ce9','#6ec2fc'],
                legend: {
                    data: ['用户', '用户量']
                },
                radar: {
                    // shape: 'circle',
                    name: {
                        textStyle: {
                            color: '#333',
                            borderRadius: 3,
                            padding: [3, 5]
                        }
                    },
                    indicator: [
                        { name: '一月', max: 6500},
                        { name: '六月', max: 16000},
                        { name: '五月', max: 30000},
                        { name: '四月', max: 38000},
                        { name: '三月', max: 52000},
                        { name: '二月', max: 25000}
                    ],
                },
                series: [{
                    name: '用户vs用户量',
                    type: 'radar',
                    // areaStyle: {normal: {}},
                    data : [
                        {
                            value : [4300, 10000, 28000, 35000, 50000, 19000],
                            name : '用户',
                            areaStyle: {
                                normal: {
                                    opacity: 0.9,
                                }
                            }
                        },
                        {
                            value : [5000, 14000, 28000, 31000, 42000, 21000],
                            name : '用户量',
                            areaStyle: {
                                normal: {
                                    opacity: 0.9,
                                }
                            }
                        }
                    ]
                }],
                // 还
                huanData: {
                    columns: ['产品', '数量'],
                    rows: [
                        { '产品': '西安', '数量': 2393 },
                        { '产品': '北京', '数量': 2030 },
                        { '产品': '杭州', '数量': 2923 },
                        { '产品': '上海', '数量': 1723 },
                        { '产品': '深圳', '数量': 3092 },
                    ],

                },
                yhData: {
                    columns: ['产品', '数量'],
                    rows: [
                        { '产品': 'APP', '数量': 2030 },
                        { '产品': 'WEB端', '数量': 2923 },
                        { '产品': '移动端', '数量': 1723 },
                    ],

                },
                url: 'https://img.alicdn.com/bao/uploaded/i3/2262300335/O1CN019fEmXK1ELTDgkTz8b_!!0-item_pic.jpg',
                srcList: [
                    'https://img.alicdn.com/bao/uploaded/i3/2262300335/O1CN019fEmXK1ELTDgkTz8b_!!0-item_pic.jpg',
                    'https://img.alicdn.com/bao/uploaded/i3/2262300335/O1CN019fEmXK1ELTDgkTz8b_!!0-item_pic.jpg'
                ],
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
        /*float: left;*/
        display: flex;
        width: auto;
        margin: 10px 0;
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

    .s-box{
        display: flex;
        justify-content: space-between;
    }
    .xz{
        display: flex;
        margin-right: 10px;
        cursor: pointer;
    }
    .xz i{
        line-height: 40px;
        color: #67c1fd;
        margin-right: 4px;
    }
    .xz h6{
        line-height: 40px;
        /*font-weight: 400;*/
    }
    .xx-box span{
        margin-bottom: 30px;
    }
</style>
