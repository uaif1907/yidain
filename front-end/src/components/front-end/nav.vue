<template>
    <div class="nav-box">
        <el-row :span="24">
            <el-col :span="4" style="height: 80px">
                <div class="box">
                    <i class="logo"></i>
                    <div class="size">
                        <span>一点生活</span>
                        <span>A LITTLE LIFE</span>
                    </div>
                </div>
            </el-col>
            <el-col :span="16" style="height: 80px">
                <el-row :span="24">
                    <el-col :span="22" style="height: 80px;float: right;">
                        <el-row :span="24">
                            <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" active-text-color="#333333" style="display:flex;height: 80px;justify-content: space-between">
                                <el-menu-item index="1">
                                    <router-link :to="{name:'first'}" tag="div">
                                        <p style="height: 20px">全部</p>
                                        <p class="zi">All</p>
                                    </router-link>
                                </el-menu-item>
                                <el-menu-item index="2">
                                    <router-link :to="{name:'chair'}" tag="div">
                                        <p style="height: 20px">客厅</p>
                                        <p class="zi">Parlour</p>
                                    </router-link>
                                </el-menu-item>
                                <el-menu-item index="3">
                                    <router-link :to="{name:'bed'}" tag="div">
                                        <p style="height: 20px">厨房</p>
                                        <p class="zi">Kitchen</p>
                                    </router-link>
                                </el-menu-item>
                                <el-menu-item index="4">
                                    <router-link :to="{name:'cabinet'}" tag="div">
                                        <p style="height: 20px">卫生间</p>
                                        <p class="zi">Toilet</p>
                                    </router-link>
                                </el-menu-item>
                                <el-menu-item index="5">
                                    <router-link :to="{name:'edge'}" tag="div">
                                        <p style="height: 20px">卧室</p>
                                        <p class="zi">Bedrooml</p>
                                    </router-link>
                                </el-menu-item>
                                <el-menu-item index="6">
                                    <router-link :to="{name:'edge'}" tag="div">
                                        <p style="height: 20px">书房</p>
                                        <p class="zi">Study</p>
                                    </router-link>
                                </el-menu-item>
                                <el-menu-item index="7">
                                    <router-link :to="{name:'edge'}" tag="div">
                                        <p style="height: 20px">阳台</p>
                                        <p class="zi">Balcony</p>
                                    </router-link>
                                </el-menu-item>
                                <el-menu-item index="8">
                                    <router-link :to="{name:'edge'}" tag="div">
                                        <p style="height: 20px">餐厅</p>
                                        <p class="zi">Restaurant</p>
                                    </router-link>
                                </el-menu-item>

                            </el-menu>
                        </el-row>
                    </el-col>
                </el-row>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    // @ is an alias to /src
    // import HelloWorld from '@/components/HelloWorld.vue'

    export default {
        name: 'navs',
        components: {
            // HelloWorld
        },
        data(){
            return {
                activeIndex: '1'
            }
        },
        methods: {
            handleSelect() {
            }
        }
    }
</script>

<style scoped>
    .nav-box{
        width: 1200px;
        height: 80px;
        margin: 0 auto;
    }
    .box{
        display: flex;
        justify-content: center;
    }
    .logo{
        width: 49px;
        height: 49px;
        background: url("../../assets/list/logo.png") no-repeat;
        background-size: contain;
        margin: 12px 14px 20px 0;
    }
    .size{
        height: 32px;
        display: flex;
        flex-direction: column;
        align-content: center;
        border-left: 2px solid #7f7f7f;
        box-sizing: border-box;
        font-size: 12px;
        margin-top: 20px;
    }
    .size span{
        width: 94px;
        height: 18px;
        line-height: 18px;
        text-align: center;
    }
    .size span:first-child{
        color: #191919;
        font-weight: 600;
    }
    .size span:last-child{
        color: #7f7f7f;
    }
    .el-menu-item{
        height: 80px;
        /*line-height: 80px;*/
        text-align: center;
        padding: 0!important;
    }
    .el-menu-demo{
        border: none!important;
    }
    .el-menu-demo p:first-child{
        color: #4a4949!important;
    }
    .zi{
        color: #7f7f7f!important;
    }
</style>
