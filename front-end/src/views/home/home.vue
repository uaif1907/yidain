<template xmlns:el-col="http://www.w3.org/1999/html">
    <div class="home-box">
        <el-row :span="24">
            <el-col :span="14" class="tu-box">
                <div class="size">
                    <span></span>
                    <h4>销量统计</h4>
                    <span></span>
                </div>
                <ve-line :data="chartData" :settings="chartSettings" :legend="legend" :colors="color"></ve-line>
            </el-col>
            <el-col :span="8" class="map-box">
                <div class="size">
                    <span></span>
                    <h4>用户分布</h4>
                    <span></span>
                </div>
                <ve-map :data="mapData" :settings="mapSettings" :legend="{bottom:20}" :colors="color"></ve-map>
            </el-col>
        </el-row>
        <!--        下面-->
        <el-row :span="24">
            <el-col :span="14" class="cad">
                <el-col :span="7" class="caid-box">
                    <el-card class="box-card">
                        <div class="text item">
                            <h4 style="font-weight: 400;text-align: left;color: #ffffff">新增订单</h4>
                            <div class="z-box">
                                <i class="el-icon-date"></i>
                                <h1>400</h1>
                                <p>个</p>
                            </div>
                        </div>
                    </el-card>
                    <div style="background-color: white;margin-top: 10px;margin-right: 10px">
                        <div class="size">
                            <span></span>
                            <h4>订单统计量</h4>
                            <span></span>
                        </div>
                        <ve-histogram :data="zhuData" :settings="zhuSettings" :legend="legend" :colors="color" :tooltip="{trigger:'item'}"></ve-histogram>
                    </div>

                </el-col>
                <el-col :span="7" class="caid-box">
                    <el-card class="box-card jb-box">
                        <div class="text item">
                            <h4 style="font-weight: 400;text-align: left;color: #ffffff">新增访问量</h4>
                            <div class="z-box">
                                <i class="el-icon-tickets"></i>
                                <h1>359</h1>
                                <p>次</p>
                            </div>
                        </div>
                    </el-card>
                    <div style="background-color: white;margin-top: 10px">
                        <div class="size">
                            <span></span>
                            <h4>注册用户</h4>
                            <span></span>
                        </div>
                        <ve-histogram :data="ceData" :settings="ceSettings" :legend="legend" :colors="['#d177e9']" :tooltip="{trigger:'item'}"></ve-histogram>
                    </div>
                </el-col>
            </el-col>
            <el-col :span="8" style="background-color: white;margin-top: 50px">
                <div class="size">
                    <span></span>
                    <h4>产品统计</h4>
                    <span></span>
                </div>
                <ve-ring :data="huanData" :settings="huanSettings" :legend="{bottom:10}" :extend="chartExtend"></ve-ring>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    export default {
        name: 'Home',
        props: {
            // msg: String
        },
        data(){
            this.chartSettings = {
                stack: { '用户': ['访问用户', '下单用户'] },
                area: true
            };
            //地图
            this.mapSettings = {
                position: 'china',
                dimension: '位置',
                metrics: ['用户人数最多', '用户人数较多', '用户人数稀少'],
                dataType: {
                    '面积': 'KMB'
                },
                itemStyle: {
                    // 'areaColor': '#60d0dd'
                    normal: {
                        areaColor: '#60d0dd',//背景色
                        borderColor: '#0066ba'
                    },
                    emphasis: {
                        borderWidth: 0,
                        borderColor: '#0066ba',//选中颜色
                        areaColor: "#0494e1",
                        shadowColor: 'rgba(0, 0, 0, 0.5)'//阴影
                    }
                }
            };
            //柱状图
            this.zhuSettings = {
                metrics: ['订单量'],
                dimension: ['日期'],
                itemStyle: {
                    barBorderRadius: [50, 50, 0, 0],
                }
            };
            //柱状图2
            this.ceSettings = {
                metrics: ['人数'],
                dimension: ['日期'],
                itemStyle: {
                    barBorderRadius: [50, 50, 0, 0],
                }
            };
            //换图
            this.huanSettings = {
                dimension: '产品',
                metrics: '数量',
                radius: ['60px', '80px'],
                label: {
                    formatter: params => {
                        if (params.dataIndex === 0) {
                            return `{a| 床具${params.percent}%}`
                        } else if (params.dataIndex === 1){
                            return `{b| 厨具${params.percent}%}`
                        } else if (params.dataIndex === 2){
                            return `{c| 灯具${params.percent}%}`
                        } else if (params.dataIndex === 3){
                            return `{d| 沙发${params.percent}%}`
                        } else {
                            return `{e| 座椅${params.percent}%}`
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
            return {
                color:['#65bbfc','#da87ec','#e26172'],
                legend:{
                    right:30,top:10,bottom:10
                },
                chartData: {
                    columns: ['时间', '昨日销量', '今日销量'],
                    rows: [
                        { '时间': '04:00', '昨日销量': 2093, '今日销量': 1093,  },
                        { '时间': '06:00', '昨日销量': 3530, '今日销量': 2230,  },
                        { '时间': '08:00', '昨日销量': 2923, '今日销量': 2623,  },
                        { '时间': '10:00', '昨日销量': 1723, '今日销量': 1423,  },
                        { '时间': '12:00', '昨日销量': 1500, '今日销量': 2500,  },
                        { '时间': '14:00', '昨日销量': 2200, '今日销量': 1200,  },
                        { '时间': '16:00', '昨日销量': 3792, '今日销量': 2492,  },
                        { '时间': '18:00', '昨日销量': 2792, '今日销量': 3002,  },
                        { '时间': '20:00', '昨日销量': 3792, '今日销量': 2122,  },
                        { '时间': '22:00', '昨日销量': 3592, '今日销量': 4002,  },
                    ]
                },
                mapData: {
                    columns: ['位置', '用户人数最多', '用户人数较多', '用户人数稀少'],
                    rows: [
                        { '位置': '吉林', '用户人数稀少': 92134 },
                        { '位置': '北京', '用户人数较多': 2123 },
                        { '位置': '上海', '用户人数稀少': 94234 },
                        { '位置': '浙江', '用户人数较多': 5123 },
                        { '位置': '内蒙古', '用户人数最多': 4123 },
                        { '位置': '西藏', '用户人数较多': 4123 },
                        { '位置': '湖北', '用户人数较多': 4123 }
                    ]
                },
                //柱状图
                zhuData: {
                    columns: ['日期', '订单量'],
                    rows: [
                        { '日期': '1', '订单量': 1393, },
                        { '日期': '2', '订单量': 1930, },
                        { '日期': '3', '订单量': 2423, },
                        { '日期': '4', '订单量': 2723, },
                        { '日期': '5', '订单量': 3192, },
                        { '日期': '6', '订单量': 3593, },
                        { '日期': '7', '订单量': 3192, },
                        { '日期': '8', '订单量': 2723, },
                        { '日期': '9', '订单量': 2423, },
                        { '日期': '10', '订单量': 1930, },
                        { '日期': '11', '订单量': 1393, },
                        { '日期': '12', '订单量': 1000, }
                    ]
                },
                ceData: {
                    columns: ['日期', '人数'],
                    rows: [
                        { '日期': '1', '人数': 1393, },
                        { '日期': '2', '人数': 1930, },
                        { '日期': '3', '人数': 2423, },
                        { '日期': '4', '人数': 2723, },
                        { '日期': '5', '人数': 3192, },
                        { '日期': '6', '人数': 3593, },
                        { '日期': '7', '人数': 3192, },
                        { '日期': '8', '人数': 2723, },
                        { '日期': '9', '人数': 2423, },
                        { '日期': '10', '人数': 1930, },
                        { '日期': '11', '人数': 1393, },
                        { '日期': '12', '人数': 1000, }
                    ]
                },
                //环图
                huanData: {
                    columns: ['产品', '数量'],
                    rows: [
                        { '产品': '床具', '数量': 2393 },
                        { '产品': '厨具', '数量': 2030 },
                        { '产品': '灯具', '数量': 2923 },
                        { '产品': '沙发', '数量': 1723 },
                        { '产品': '座椅', '数量': 3092 },
                    ],

                }
            }
        },
        methods: {
            handleSelect() {
            },
            handleClose() {
            }
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .home-box{
    }
    .tu-box{
        background-color: #ffffff!important;
        margin-right: 25px;
        margin-bottom: 10px;
    }
    .map-box{
        padding-left: 20px;
        box-sizing: border-box;
        background-color: #ffffff!important;
    }
    .size{
        position: relative;
        left: 12px;
        top: 30px;
        display: inline-block;
        float: left;
        display: flex;
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
    .cad{
        display: flex;
        margin-right: 25px;
    }
    .caid-box{
        width: 100%;
    }
    .el-card{
        background: -webkit-linear-gradient(left,#67c1fd,#71dcfd);
        border: none!important;
        border-radius: 20px;
        margin-right: 10px;
    }

    .z-box{
        display: flex;
        margin-top: 20px;
    }
    .el-icon-date{
        font-size: 80px;
        color: #ffffff;
        opacity: 0.5;
        margin-right: 30px;
    }
    .z-box h1{
        font-size: 50px;
        color: #ffffff;
        font-weight: 400;
        line-height: 80px;
    }
    .z-box p{
        color: white;
        margin-left: 5px;
        padding-top: 40px;
    }
    .el-icon-tickets{
        font-size: 80px;
        color: #ffffff;
        opacity: 0.5;
        margin-right: 30px;
    }
    .jb-box{
        background: -webkit-linear-gradient(left,#c975e6,#ee81ea);
        border: none!important;
        border-radius: 20px;
    }
</style>
<!---->