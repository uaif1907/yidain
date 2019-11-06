<template>
    <div class="header-box">
        <el-row :span="24">
            <el-col :span="10" class="right-box">
                <el-row :span="24">
                    <el-col :span="10" class="login-box">
                        <p>请您</p>
                        <div class="round-box">
                            <router-link :to="{name:'login'}" tag="span">登录</router-link>
                            |
                            <router-link :to="{name:'login'}" tag="span">注册</router-link>
                        </div>
                    </el-col>
                    <el-col :span="10" style="float: right;cursor: pointer">
                        <el-row :span="24">
                            <el-col :span="6">
                                <i class="el-icon-search"></i>
                            </el-col>
                            <router-link :to="{name:'shopcar'}" tag="div">
                                <el-col :span="6">
                                    <i class="el-icon-shopping-bag-2"></i>
                                </el-col>
                            </router-link>
                            <router-link :to="{name:'person'}" tag="div">
                                <el-col :span="6">
                                    <i class="el-icon-s-custom"></i>
                                </el-col>
                            </router-link>

                            <el-col :span="6">
                                <i class="el-icon-star-off"></i>
                            </el-col>
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
        name: 'headers',
        components: {
            // HelloWorld
        }
    }
</script>
<style scoped>
    .header-box{
        width: 1200px;
        margin: 0 auto;
    }
    .right-box{
        float: right;
    }
    .login-box{
        display: flex;
        margin-left: 80px;
    }
    .login-box p{
        color: #858585;
    }
    .round-box{
        height: 30px;
        width: 124px;
        margin: auto 20px;
        padding: 0!important;
        border-radius: 30px;
        border: 1px solid #8c8c8c;
        line-height: 30px;
        cursor: pointer;
        font-size: 14px;
        font-weight: 500;
    }
    i{
        font-size: 20px;
    }
</style>
