<template>
    <div class="header-box">

        <el-col :span="24">
            <el-menu class="el-menu-demo" mode="horizontal" @select="handleSelect">
                <el-menu-item index="1">
                    <i class="el-icon-bell"></i>
                </el-menu-item>
                <el-submenu index="2" class="er">
                    <template slot="title">
                        <i class="el-icon-s-operation"></i>
                    </template>
                    <el-menu-item index="2-1">
                        <i class="el-icon-s-tools"></i>设置</el-menu-item>
                    <el-menu-item index="2-2">
                        <i class="el-icon-question"></i>帮助中心</el-menu-item>
                </el-submenu>
                <el-submenu index="3">
                    <template slot="title">
                        <el-avatar size="small" :src="circleUrl"></el-avatar>
                    </template>
                    <el-menu-item index="3-1">
                        <i class="el-icon-edit-outline"></i>修改密码</el-menu-item>
                    <el-menu-item index="3-2">
                        <i class="el-icon-edit"></i>修改资料</el-menu-item>
                    <el-menu-item index="3-3">
                        <i class="el-icon-switch-button"></i>退出登录</el-menu-item>
                </el-submenu>
            </el-menu>
        </el-col>

    </div>
</template>

<script>
    export default {
        name: 'Header',
        props: {
            // msg: String
        },
        data(){
            return {
                circleUrl:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
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

.el-menu-demo{
    float: right;
}

</style>
