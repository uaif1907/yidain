<template>
    <div class="list-box">
        <!--    轮播-->
        <el-carousel class="banner-box">
            <el-carousel-item v-for="item in 4" :key="item">
            </el-carousel-item>
        </el-carousel>
        <!--查询-->
        <el-row :span="24" style="height: auto;">
            <el-row :span="24" style="height: 124px;padding: 30px 0">
                <el-col :span="6" style="display: flex">
                    <span class="round"></span>
                    <el-col :span="10">
                        <div class="tu-box">
                            <i class="el-icon-arrow-up"></i>
                            <i class="el-icon-arrow-down"></i>
                            <i class="el-icon-arrow-up"></i>
                            <i class="el-icon-arrow-down"></i>
                        </div>
                        <el-breadcrumb separator="/" class="size-box">
                            <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
                            <el-breadcrumb-item :to="{ name:'balcony'}">阳台</el-breadcrumb-item>
                        </el-breadcrumb>
                        <div class="tu-box">
                            <i class="el-icon-arrow-up"></i>
                            <i class="el-icon-arrow-down"></i>
                        </div>
                    </el-col>
                </el-col>
            </el-row>
            <el-row :span="24" style="height: auto">
                <el-form ref="form" :model="form" label-width="80px" class="form-box">
                    <el-col :span="10" class="input-box">
                        <el-form-item label="排序">
                            <el-select v-model="form.region" placeholder="请选择排序方式" style="border-radius: 20px;float: left;">
                                <el-option label="按销量排序" value="sales"></el-option>
                                <el-option label="按价格排序" value="price"></el-option>
                            </el-select>
                        </el-form-item>
                    </el-col>
                    <el-col :span="10" class="input-box">
                        <el-form-item label="价格">
                            <el-col :span="11">
                                <el-input v-model="form.pricel" placeholder="请输入价格" style="width: 134px"></el-input>
                            </el-col>
                            <el-col class="line" :span="2">-</el-col>
                            <el-col :span="11">
                                <el-input v-model="form.pricer" placeholder="请输入价格" style="width: 134px"></el-input>
                            </el-col>
                        </el-form-item>
                    </el-col>
                    <el-col :span="24">
                        <div class="tu-box" style="margin-left: 50px!important;">
                            <i class="el-icon-arrow-up"></i>
                            <i class="el-icon-arrow-down"></i>
                            <i class="el-icon-arrow-up"></i>
                            <i class="el-icon-arrow-down"></i>
                        </div>
                        <el-col style="display: flex;justify-content: space-around;margin-left: 50px;" :span="4">
                            <div>阳台：</div>
                            <div @click="airers()" style="cursor: pointer">晾衣架</div>|
                            <div @click="hooks()" style="cursor: pointer">挂钩</div>
                        </el-col>
                        <div class="tu-box" style="margin-top: 24px;margin-left: 50px">
                            <i class="el-icon-arrow-up"></i>
                            <i class="el-icon-arrow-down"></i>
                        </div>
                        <!--晾衣架-->
                        <el-col :span="24" style="display: flex; margin-top: 10px;flex-wrap: wrap;justify-content: space-around">
                            <transition name="el-fade-in-linear">
                                <el-col :span="10" v-show="airer" class="transition-box">
                                    <el-form-item label="种类" prop="zle">
                                        <el-radio-group v-model="zle" style="margin-bottom: 20px;" class="button-box">
                                            <el-radio-button :label="true">可折叠</el-radio-button>
                                            <el-radio-button :label="false">悬挂式</el-radio-button>
                                        </el-radio-group>
                                    </el-form-item>
                                </el-col>
                            </transition>
                            <transition name="el-fade-in-linear">
                                <el-col :span="10" v-show="airer" class="transition-box">
                                    <el-form-item label="材质" prop="caiz">
                                        <el-radio-group v-model="caiz" style="margin-bottom: 20px;" class="button-box">
                                            <el-radio-button :label="true">塑料</el-radio-button>
                                            <el-radio-button :label="false">不锈钢</el-radio-button>
                                            <el-radio-button>木架</el-radio-button>
                                        </el-radio-group>
                                    </el-form-item>
                                </el-col>
                            </transition>
                        </el-col>
                        <!--挂钩-->
                        <el-col :span="24" style="display: flex; flex-wrap: wrap;justify-content: space-around">
                            <transition name="el-fade-in-linear">
                                <el-col :span="10" v-show="hook" class="transition-box">
                                    <el-form-item label="材质" prop="cz">
                                        <el-radio-group v-model="cz" style="margin-bottom: 20px;" class="button-box">
                                            <el-radio-button :label="true">不锈钢</el-radio-button>
                                            <el-radio-button :label="false">竹子</el-radio-button>
                                        </el-radio-group>
                                    </el-form-item>
                                </el-col>
                            </transition>
                            <transition name="el-fade-in-linear">
                                <el-col :span="10" v-show="hook" class="">
                                    <el-form-item label="种类" prop="zl">
                                        <el-radio-group v-model="zl" style="margin-bottom: 20px;" class="button-box">
                                            <el-radio-button :label="true">单挂钩</el-radio-button>
                                            <el-radio-button :label="false">双挂钩</el-radio-button>
                                            <el-radio-button>排衣钩</el-radio-button>
                                        </el-radio-group>
                                    </el-form-item>
                                </el-col>
                            </transition>
                        </el-col>
                    </el-col>

                </el-form>
            </el-row>
        </el-row>
        <!--列表-->
        <el-row :span="24" style="height: 410px;display: flex;justify-content: space-between;margin-top: 60px">
            <el-col :span="12" style="position: relative;cursor: pointer" class="img-box">
                <img src="../../../assets/list/t1.png" alt="">
                <div class="xiaoyao-box">
                    <el-row class="gang-box"></el-row>
                    <el-row class="mahouse-box">MAHOUSE</el-row>
                    <el-row class="ws-box">午睡逍遥椅</el-row>
                    <el-row class="give-box">Give you a truly relaxing</el-row>
                    <el-row class="and-box">and comfortable experience.</el-row>
                    <el-row class="jg-box">
                        <el-col>1029.00</el-col>
                        <el-col class="rmb-box">RMB</el-col>
                    </el-row>
                    <el-row class="btn-box">
                        <el-button style="background-color: #5ed5e0;border: 1px solid #5ed5e0!important;color: white;padding: 10px 20px">GO</el-button>
                    </el-row>
                </div>
            </el-col>
            <!--            第二个图-->
            <el-col :span="6" style="position: relative;" class="ying-box">
                <router-link tag="div" :to="{name:'details'}">
                    <el-col class="gwc-box">
                        <i class="iconfont icon-gouwuche"></i>
                    </el-col>
                    <el-col class="gg-box"></el-col>
                    <el-col class="yc-box"></el-col>
                    <el-row :span="24" style="display: flex;flex-wrap: wrap;cursor: pointer;">
                        <el-col :span="20" class="yz-box"></el-col>
                        <el-col :span="24" class="bun-box">
                            <el-row :span="24" style="display: flex;flex-wrap: wrap">
                                <el-col class="g-box"></el-col>
                                <el-col class="zest-box">ZEST ONE</el-col>
                                <el-col>
                                    <el-row>
                                        <el-col style="display: flex;justify-content: center;line-height: 20px">
                                            <i class="el-icon-arrow-up" style="line-height: 20px;color: #7f7f7f"></i>
                                            <span style="margin: 0 4px;color: #272727;font-weight: 600">装饰椅</span>
                                            <i class="el-icon-arrow-up" style="line-height: 20px;color: #7f7f7f"></i>
                                        </el-col>
                                    </el-row>
                                </el-col>
                                <el-col class="xd-box">现代小椅，随处安放的舒适</el-col>
                                <el-col style="display: flex;justify-content: center">
                                    <el-row class="r-box">RMB</el-row>
                                    <el-row class="w-box">599.00</el-row>
                                </el-col>
                            </el-row>
                        </el-col>
                    </el-row>
                </router-link>
            </el-col>
            <!--            第三个图-->
            <el-col :span="6" style="position: relative;" class="ying-box">
                <router-link tag="div" :to="{name:'details'}">
                    <el-col class="gwc-box">
                        <i class="iconfont icon-gouwuche"></i>
                    </el-col>
                    <el-col class="gg-box"></el-col>
                    <el-col class="yc-box"></el-col>
                    <el-row :span="24" style="display: flex;flex-wrap: wrap;cursor: pointer;">
                        <el-col :span="20" class="yz-box yz-box1"></el-col>
                        <el-col :span="24" class="bun-box">
                            <el-row :span="24" style="display: flex;flex-wrap: wrap">
                                <el-col class="g-box"></el-col>
                                <el-col class="zest-box">MORNING TWILIGHT</el-col>
                                <el-col>
                                    <el-row>
                                        <el-col style="display: flex;justify-content: center;line-height: 20px">
                                            <i class="el-icon-arrow-up" style="line-height: 20px;color: #7f7f7f"></i>
                                            <span style="margin: 0 4px;color: #272727;font-weight: 600">晨暮青</span>
                                            <i class="el-icon-arrow-up" style="line-height: 20px;color: #7f7f7f"></i>
                                        </el-col>
                                    </el-row>
                                </el-col>
                                <el-col class="xd-box">脱开引力，自由旋转</el-col>
                                <el-col style="display: flex;justify-content: center">
                                    <el-row class="r-box">RMB</el-row>
                                    <el-row class="w-box">499.00</el-row>
                                </el-col>
                            </el-row>
                        </el-col>
                    </el-row>
                </router-link>
            </el-col>
        </el-row>
        <!--第二-->
        <el-row :span="24" style="height: 410px;display: flex;justify-content: space-between;margin-top: 60px">
            <el-col :span="6" style="position: relative;" class="ying-box">
                <router-link tag="div" :to="{name:'details'}">
                    <el-col class="gwc-box">
                        <i class="iconfont icon-gouwuche"></i>
                    </el-col>
                    <el-col class="gg-box"></el-col>
                    <el-col class="yc-box"></el-col>
                    <el-row :span="24" style="display: flex;flex-wrap: wrap;cursor: pointer;">
                        <el-col :span="20" class="yz-box yz-box4"></el-col>
                        <el-col :span="24" class="bun-box">
                            <el-row :span="24" style="display: flex;flex-wrap: wrap">
                                <el-col class="g-box"></el-col>
                                <el-col class="zest-box">WINDSOR CHAIR</el-col>
                                <el-col>
                                    <el-row>
                                        <el-col style="display: flex;justify-content: center;line-height: 20px">
                                            <i class="el-icon-arrow-up" style="line-height: 20px;color: #7f7f7f"></i>
                                            <span style="margin: 0 4px;color: #272727;font-weight: 600">温莎椅</span>
                                            <i class="el-icon-arrow-up" style="line-height: 20px;color: #7f7f7f"></i>
                                        </el-col>
                                    </el-row>
                                </el-col>
                                <el-col class="xd-box">设计简单而不是尊贵</el-col>
                                <el-col style="display: flex;justify-content: center">
                                    <el-row class="r-box">RMB</el-row>
                                    <el-row class="w-box">460.00</el-row>
                                </el-col>
                            </el-row>
                        </el-col>
                    </el-row>
                </router-link>
            </el-col>
            <el-col :span="6" style="position: relative;" class="ying-box">
                <router-link tag="div" :to="{name:'details'}">
                    <el-col class="gwc-box">
                        <i class="iconfont icon-gouwuche"></i>
                    </el-col>
                    <el-col class="gg-box"></el-col>
                    <el-col class="yc-box"></el-col>
                    <el-row :span="24" style="display: flex;flex-wrap: wrap;cursor: pointer;">
                        <el-col :span="20" class="yz-box yz-box5"></el-col>
                        <el-col :span="24" class="bun-box">
                            <el-row :span="24" style="display: flex;flex-wrap: wrap">
                                <el-col class="g-box"></el-col>
                                <el-col class="zest-box">LUXURY DINING CHAIR</el-col>
                                <el-col>
                                    <el-row>
                                        <el-col style="display: flex;justify-content: center;line-height: 20px">
                                            <i class="el-icon-arrow-up" style="line-height: 20px;color: #7f7f7f"></i>
                                            <span style="margin: 0 4px;color: #272727;font-weight: 600">轻奢餐椅</span>
                                            <i class="el-icon-arrow-up" style="line-height: 20px;color: #7f7f7f"></i>
                                        </el-col>
                                    </el-row>
                                </el-col>
                                <el-col class="xd-box">不止黑白灰的高雅</el-col>
                                <el-col style="display: flex;justify-content: center">
                                    <el-row class="r-box">RMB</el-row>
                                    <el-row class="w-box">539.00</el-row>
                                </el-col>
                            </el-row>
                        </el-col>
                    </el-row>
                </router-link>
            </el-col>
            <!--            第3个图-->
            <el-col :span="6" style="position: relative;" class="ying-box">
                <router-link tag="div" :to="{name:'details'}">
                    <el-col class="gwc-box">
                        <i class="iconfont icon-gouwuche"></i>
                    </el-col>
                    <el-col class="gg-box"></el-col>
                    <el-col class="yc-box"></el-col>
                    <el-row :span="24" style="display: flex;flex-wrap: wrap;cursor: pointer;">
                        <el-col :span="20" class="yz-box yz-box6"></el-col>
                        <el-col :span="24" class="bun-box">
                            <el-row :span="24" style="display: flex;flex-wrap: wrap">
                                <el-col class="g-box"></el-col>
                                <el-col class="zest-box">CASTLE PEAK CHAIR</el-col>
                                <el-col>
                                    <el-row>
                                        <el-col style="display: flex;justify-content: center;line-height: 20px">
                                            <i class="el-icon-arrow-up" style="line-height: 20px;color: #7f7f7f"></i>
                                            <span style="margin: 0 4px;color: #272727;font-weight: 600">青山椅</span>
                                            <i class="el-icon-arrow-up" style="line-height: 20px;color: #7f7f7f"></i>
                                        </el-col>
                                    </el-row>
                                </el-col>
                                <el-col class="xd-box">抽离繁琐的设计，体现美的线条</el-col>
                                <el-col style="display: flex;justify-content: center">
                                    <el-row class="r-box">RMB</el-row>
                                    <el-row class="w-box">599.00</el-row>
                                </el-col>
                            </el-row>
                        </el-col>
                    </el-row>
                </router-link>
            </el-col>
            <!--            第4个图-->
            <el-col :span="6" style="position: relative;" class="ying-box">
                <router-link tag="div" :to="{name:'details'}">
                    <el-col class="gwc-box">
                        <i class="iconfont icon-gouwuche"></i>
                    </el-col>
                    <el-col class="gg-box"></el-col>
                    <el-col class="yc-box"></el-col>
                    <el-row :span="24" style="display: flex;flex-wrap: wrap;cursor: pointer;">
                        <el-col :span="20" class="yz-box yz-box7"></el-col>
                        <el-col :span="24" class="bun-box">
                            <el-row :span="24" style="display: flex;flex-wrap: wrap">
                                <el-col class="g-box"></el-col>
                                <el-col class="zest-box">CONCH CHAIR</el-col>
                                <el-col>
                                    <el-row>
                                        <el-col style="display: flex;justify-content: center;line-height: 20px">
                                            <i class="el-icon-arrow-up" style="line-height: 20px;color: #7f7f7f"></i>
                                            <span style="margin: 0 4px;color: #272727;font-weight: 600">海螺椅</span>
                                            <i class="el-icon-arrow-up" style="line-height: 20px;color: #7f7f7f"></i>
                                        </el-col>
                                    </el-row>
                                </el-col>
                                <el-col class="xd-box">现代小椅，随处安放的舒适</el-col>
                                <el-col style="display: flex;justify-content: center">
                                    <el-row class="r-box">RMB</el-row>
                                    <el-row class="w-box">588.00</el-row>
                                </el-col>
                            </el-row>
                        </el-col>
                    </el-row>
                </router-link>
            </el-col>
        </el-row>
        <!--第3-->
        <el-row :span="24" style="height: 410px;display: flex;justify-content: space-between;margin-top: 60px">
            <el-col :span="6" style="position: relative;" class="ying-box">
                <router-link tag="div" :to="{name:'details'}">
                    <el-col class="gwc-box">
                        <i class="iconfont icon-gouwuche"></i>
                    </el-col>
                    <el-col class="gg-box"></el-col>
                    <el-col class="yc-box"></el-col>
                    <el-row :span="24" style="display: flex;flex-wrap: wrap;cursor: pointer;">
                        <el-col :span="20" class="yz-box yz-box8"></el-col>
                        <el-col :span="24" class="bun-box">
                            <el-row :span="24" style="display: flex;flex-wrap: wrap">
                                <el-col class="g-box"></el-col>
                                <el-col class="zest-box">WINDSOR CHAIR</el-col>
                                <el-col>
                                    <el-row>
                                        <el-col style="display: flex;justify-content: center;line-height: 20px">
                                            <i class="el-icon-arrow-up" style="line-height: 20px;color: #7f7f7f"></i>
                                            <span style="margin: 0 4px;color: #272727;font-weight: 600">温莎椅</span>
                                            <i class="el-icon-arrow-up" style="line-height: 20px;color: #7f7f7f"></i>
                                        </el-col>
                                    </el-row>
                                </el-col>
                                <el-col class="xd-box">设计简单而不是尊贵</el-col>
                                <el-col style="display: flex;justify-content: center">
                                    <el-row class="r-box">RMB</el-row>
                                    <el-row class="w-box">460.00</el-row>
                                </el-col>
                            </el-row>
                        </el-col>
                    </el-row>
                </router-link>
            </el-col>
            <el-col :span="6" style="position: relative;" class="ying-box">
                <router-link tag="div" :to="{name:'details'}">
                    <el-col class="gwc-box">
                        <i class="iconfont icon-gouwuche"></i>
                    </el-col>
                    <el-col class="gg-box"></el-col>
                    <el-col class="yc-box"></el-col>
                    <el-row :span="24" style="display: flex;flex-wrap: wrap;cursor: pointer;">
                        <el-col :span="20" class="yz-box yz-box9"></el-col>
                        <el-col :span="24" class="bun-box">
                            <el-row :span="24" style="display: flex;flex-wrap: wrap">
                                <el-col class="g-box"></el-col>
                                <el-col class="zest-box">CHUN MU HOME</el-col>
                                <el-col>
                                    <el-row>
                                        <el-col style="display: flex;justify-content: center;line-height: 20px">
                                            <i class="el-icon-arrow-up" style="line-height: 20px;color: #7f7f7f"></i>
                                            <span style="margin: 0 4px;color: #272727;font-weight: 600">春沐椅</span>
                                            <i class="el-icon-arrow-up" style="line-height: 20px;color: #7f7f7f"></i>
                                        </el-col>
                                    </el-row>
                                </el-col>
                                <el-col class="xd-box">写意太师、蕴照东方</el-col>
                                <el-col style="display: flex;justify-content: center">
                                    <el-row class="r-box">RMB</el-row>
                                    <el-row class="w-box">1290.00</el-row>
                                </el-col>
                            </el-row>
                        </el-col>
                    </el-row>
                </router-link>
            </el-col>
            <!--            第3个图-->
            <el-col :span="6" style="position: relative;" class="h-box">
                <router-link tag="div" :to="{name:'details'}">
                    <img src="../../../assets/list/t10.png" alt="">
                    <el-col :span="24" class="bj-box"></el-col>
                    <el-col :span="20" class="ye-box">
                        <el-col class="ha-box">HAMMARN</el-col>
                        <el-col class="ma-box">哈马恩</el-col>
                        <el-col class="en-box">Hammarn</el-col>
                    </el-col>
                    <el-col :span="24" class="xia-box">
                        <el-row :span="24" style="display: flex">
                            <el-col style="display: flex;">
                                <el-col class="er-box">268.00</el-col>
                                <el-col class="q-box">RMB</el-col>
                            </el-col>
                            <el-col>
                                <el-button style="padding: 9px 20px;float: right;border: 1px solid #999999">Buy</el-button>
                            </el-col>
                        </el-row>
                    </el-col>
                </router-link>
            </el-col>
            <!--            第4个图-->
            <el-col :span="6" style="position: relative;" class="ying-box">
                <router-link tag="div" :to="{name:'details'}">
                    <el-col class="gwc-box">
                        <i class="iconfont icon-gouwuche"></i>
                    </el-col>
                    <el-col class="gg-box"></el-col>
                    <el-col class="yc-box"></el-col>
                    <el-row :span="24" style="display: flex;flex-wrap: wrap;cursor: pointer;">
                        <el-col :span="20" class="yz-box yz-box11"></el-col>
                        <el-col :span="24" class="bun-box">
                            <el-row :span="24" style="display: flex;flex-wrap: wrap">
                                <el-col class="g-box"></el-col>
                                <el-col class="zest-box">LAZY CHAIR.</el-col>
                                <el-col>
                                    <el-row>
                                        <el-col style="display: flex;justify-content: center;line-height: 20px">
                                            <i class="el-icon-arrow-up" style="line-height: 20px;color: #7f7f7f"></i>
                                            <span style="margin: 0 4px;color: #272727;font-weight: 600">懒人椅子</span>
                                            <i class="el-icon-arrow-up" style="line-height: 20px;color: #7f7f7f"></i>
                                        </el-col>
                                    </el-row>
                                </el-col>
                                <el-col class="xd-box">拉丝不锈钢金属架，值得你选择</el-col>
                                <el-col style="display: flex;justify-content: center">
                                    <el-row class="r-box">RMB</el-row>
                                    <el-row class="w-box">888.00</el-row>
                                </el-col>
                            </el-row>
                        </el-col>
                    </el-row>
                </router-link>
            </el-col>
        </el-row>
        <!--第4-->
        <el-row :span="24" style="height: 410px;display: flex;justify-content: space-between;margin-top: 60px">
            <el-col :span="6" style="position: relative;" class="ying-box">
                <router-link tag="div" :to="{name:'details'}">
                    <el-col class="gwc-box">
                        <i class="iconfont icon-gouwuche"></i>
                    </el-col>
                    <el-col class="gg-box"></el-col>
                    <el-col class="yc-box"></el-col>
                    <el-row :span="24" style="display: flex;flex-wrap: wrap;cursor: pointer;">
                        <el-col :span="20" class="yz-box yz-box12"></el-col>
                        <el-col :span="24" class="bun-box">
                            <el-row :span="24" style="display: flex;flex-wrap: wrap">
                                <el-col class="g-box"></el-col>
                                <el-col class="zest-box">OBEDIENCE FUJIJO</el-col>
                                <el-col>
                                    <el-row>
                                        <el-col style="display: flex;justify-content: center;line-height: 20px">
                                            <i class="el-icon-arrow-up" style="line-height: 20px;color: #7f7f7f"></i>
                                            <span style="margin: 0 4px;color: #272727;font-weight: 600">藤条椅</span>
                                            <i class="el-icon-arrow-up" style="line-height: 20px;color: #7f7f7f"></i>
                                        </el-col>
                                    </el-row>
                                </el-col>
                                <el-col class="xd-box">设计简单而不是尊贵</el-col>
                                <el-col style="display: flex;justify-content: center">
                                    <el-row class="r-box">RMB</el-row>
                                    <el-row class="w-box">460.00</el-row>
                                </el-col>
                            </el-row>
                        </el-col>
                    </el-row>
                </router-link>
            </el-col>
            <el-col :span="6" style="position: relative;" class="ying-box">
                <router-link tag="div" :to="{name:'details'}">
                    <el-col class="gwc-box">
                        <i class="iconfont icon-gouwuche"></i>
                    </el-col>
                    <el-col class="gg-box"></el-col>
                    <el-col class="yc-box"></el-col>
                    <el-row :span="24" style="display: flex;flex-wrap: wrap;cursor: pointer;">
                        <el-col :span="20" class="yz-box yz-box13"></el-col>
                        <el-col :span="24" class="bun-box">
                            <el-row :span="24" style="display: flex;flex-wrap: wrap">
                                <el-col class="g-box"></el-col>
                                <el-col class="zest-box">NET RED CHAIR</el-col>
                                <el-col>
                                    <el-row>
                                        <el-col style="display: flex;justify-content: center;line-height: 20px">
                                            <i class="el-icon-arrow-up" style="line-height: 20px;color: #7f7f7f"></i>
                                            <span style="margin: 0 4px;color: #272727;font-weight: 600">网红椅</span>
                                            <i class="el-icon-arrow-up" style="line-height: 20px;color: #7f7f7f"></i>
                                        </el-col>
                                    </el-row>
                                </el-col>
                                <el-col class="xd-box">无任何人造板和贴皮</el-col>
                                <el-col style="display: flex;justify-content: center">
                                    <el-row class="r-box">RMB</el-row>
                                    <el-row class="w-box">540.00</el-row>
                                </el-col>
                            </el-row>
                        </el-col>
                    </el-row>
                </router-link>
            </el-col>
            <!--            第二个图-->
            <el-col :span="6" style="position: relative;" class="ying-box">
                <router-link tag="div" :to="{name:'details'}">
                    <el-col class="gwc-box">
                        <i class="iconfont icon-gouwuche"></i>
                    </el-col>
                    <el-col class="gg-box"></el-col>
                    <el-col class="yc-box"></el-col>
                    <el-row :span="24" style="display: flex;flex-wrap: wrap;cursor: pointer;">
                        <el-col :span="20" class="yz-box yz-box14"></el-col>
                        <el-col :span="24" class="bun-box">
                            <el-row :span="24" style="display: flex;flex-wrap: wrap">
                                <el-col class="g-box"></el-col>
                                <el-col class="zest-box">CASTLE PEAK CHAIR</el-col>
                                <el-col>
                                    <el-row>
                                        <el-col style="display: flex;justify-content: center;line-height: 20px">
                                            <i class="el-icon-arrow-up" style="line-height: 20px;color: #7f7f7f"></i>
                                            <span style="margin: 0 4px;color: #272727;font-weight: 600">青山椅</span>
                                            <i class="el-icon-arrow-up" style="line-height: 20px;color: #7f7f7f"></i>
                                        </el-col>
                                    </el-row>
                                </el-col>
                                <el-col class="xd-box">抽离繁琐的设计，体现美的线条</el-col>
                                <el-col style="display: flex;justify-content: center">
                                    <el-row class="r-box">RMB</el-row>
                                    <el-row class="w-box">599.00</el-row>
                                </el-col>
                            </el-row>
                        </el-col>
                    </el-row>
                </router-link>
            </el-col>
            <!--            第三个图-->
            <el-col :span="6" style="position: relative;" class="ying-box">
                <router-link tag="div" :to="{name:'details'}">
                    <el-col class="gwc-box">
                        <i class="iconfont icon-gouwuche"></i>
                    </el-col>
                    <el-col class="gg-box"></el-col>
                    <el-col class="yc-box"></el-col>
                    <el-row :span="24" style="display: flex;flex-wrap: wrap;cursor: pointer;">
                        <el-col :span="20" class="yz-box yz-box15"></el-col>
                        <el-col :span="24" class="bun-box">
                            <el-row :span="24" style="display: flex;flex-wrap: wrap">
                                <el-col class="g-box"></el-col>
                                <el-col class="zest-box">CONCH CHAIR</el-col>
                                <el-col>
                                    <el-row>
                                        <el-col style="display: flex;justify-content: center;line-height: 20px">
                                            <i class="el-icon-arrow-up" style="line-height: 20px;color: #7f7f7f"></i>
                                            <span style="margin: 0 4px;color: #272727;font-weight: 600">海螺椅</span>
                                            <i class="el-icon-arrow-up" style="line-height: 20px;color: #7f7f7f"></i>
                                        </el-col>
                                    </el-row>
                                </el-col>
                                <el-col class="xd-box">现代小椅，随处安放的舒适</el-col>
                                <el-col style="display: flex;justify-content: center">
                                    <el-row class="r-box">RMB</el-row>
                                    <el-row class="w-box">588.00</el-row>
                                </el-col>
                            </el-row>
                        </el-col>
                    </el-row>
                </router-link>
            </el-col>
        </el-row>
        <!--        分页-->
        <el-row :span="24">
            <el-col>
                <div class="block">
                    <el-pagination
                            @size-change="handleSizeChange"
                            @current-change="handleCurrentChange"
                            :current-page.sync="currentPage"
                            :page-sizes="[5, 20, 30, 40]"
                            :page-size="pageSize"
                            layout="prev, pager, next"
                            :total="total"
                    >
                    </el-pagination>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    // @ is an alias to /src

    export default {
        name: 'lists',
        components: {

        },
        data(){
            return {
                airer:false,
                hook:false,
                total:50,//默认数据总数
                currentPage:1,//默认开始页面
                pageSize:5,//每页的数据条数
                zle:true,
                caiz:true,
                cz:true,
                zl:true,
                form:{
                    region:'',
                    pricel:'',
                    pricer:'',
                }
            }
        },
        methods:{
            handleSizeChange() {
            },
            handleCurrentChange(val) {
                // console.log(`当前页: ${val}`);
                this.currentPage = val;
            },
            airers(){
                this.airer = !this.airer;
                this.hook = false;
            },
            hooks(){
                this.airer = false;
                this.hook = !this.hook;
            },
        }
    }
</script>

<style scoped>
    .list-box{
        width: 1200px;
        font-family: "Microsoft YaHei";
    }
    .el-carousel__item h3 {
        color: #475669;
        font-size: 18px;
        opacity: 0.75;
        margin: 0;
    }
    .banner-box{
        margin-top: 10px;
    }
    .el-carousel__item:nth-child(n) {
        background: url("../../../assets/list/lb1.png") no-repeat;
        background-size: 100% 100%;
    }
    .el-carousel__item:nth-child(2n) {
        background: url("../../../assets/list/lb2.png") no-repeat;
        background-size: cover;
    }
    .el-carousel__item:nth-child(3) {
        background: url("../../../assets/list/lb3.png") no-repeat;
        background-size: cover;
    }
    .el-carousel__item:nth-child(4){
        background: url("../../../assets/list/lb4.png") no-repeat;
        background-size: cover;
    }
    .banner-box{
        height: 500px!important;
    }
    .el-carousel__container{
        height: 500px!important;
    }
    .round{
        width: 10px;
        height: 10px;
        background-color: #4cc0cb;
        border-radius: 50%;
        margin: auto 20px;
    }
    .tu-box{
        width: 80px;
        height: 20px;
        display: flex;
    }
    .tu-box i{
        line-height: 20px;
        color: #cacaca;
    }
    .size-box{
        margin: 10px 0;
    }
    .el-form{
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        align-content: space-around;
        height: 332px;
    }
    .button-box{
        display: flex;
        justify-content: space-between;
    }
    .img-box{
        background: url("../../../assets/list/GreiberWhite.png");
        background-size: 100% 100%;
    }
    .img-box img{
        width: 410px;
        height: 368px;
        position: absolute;
        left: -60px;
        top: -65px;
    }
    .xiaoyao-box{
        width: 250px;
        height: 284px;
        position: absolute;
        right: 0;
        top: 40px;
        padding: 10px;
        box-sizing: border-box;
    }
    .gang-box{
        width: 16px;
        height: 4px;
        background-color: #ffca57;
        border-radius: 30px;
        margin-bottom: 18px;
    }
    .mahouse-box{
        color: #929292;
        font-weight: 600;
        text-align: left;
        font-size: 18px;
        margin-bottom: 2px;
    }
    .ws-box{
        color: #181818;
        font-weight: 600;
        text-align: left;
        font-size: 22px;
        letter-spacing:8px
    }
    .give-box{
        color: #888888;
        text-align: left;
        font-size: 12px;
        margin-top: 30px;
    }
    .and-box{
        color: #888888;
        text-align: left;
        font-size: 12px;
    }
    .jg-box{
        display: flex;
        font-size: 28px;
        color: #181818;
        margin-top: 50px;
    }
    .jg-box span{
        letter-spacing: 1px;
    }
    .rmb-box{
        color: #888888;
        font-size: 12px;
        text-align: left;
        padding-top: 18px;
        padding-left: 8px;
        box-sizing: border-box;
    }
    .btn-box{
        margin-top: 20px;
        float: left;
    }
    .yz-box{
        margin: 0 auto;
        height: 254px;
        background: url("../../../assets/list/t2.png") no-repeat;
        background-position: center center;
    }
    .bun-box{
        height: calc(410px - 254px);
    }
    .g-box{
        width: 22px;
        height: 4px;
        background-color: #ffca57;
        border-radius: 30px;
        margin: 0 auto 10px;
    }
    .zest-box{
        color: #9f9f9f;
        font-size: 18px;
        font-weight: 600;
    }
    .xd-box{
        font-size: 12px;
        color: #878787;
        margin: 20px 0;
    }
    .r-box{
        color: #707070;
        font-size: 10px;
        padding-top: 3px;
        padding-right: 2px;
        box-sizing: border-box;
    }
    .w-box{
        color: #191919;
        font-weight: 600;
        letter-spacing: 1px;
        font-size: 18px;
    }
    .yc-box{
        width: 100%;
        height: 100%;
        background-color: #f3f3f3;
        position: absolute;
        border: 4px solid white;
        box-shadow: 0 0 10px 2px #f2f2f2;
        display: none;
    }
    .gwc-box{
        width: 30px;
        height: 30px;
        z-index: 99;
        position: absolute;
        margin-top: 14px;
        margin-left: 14px;
        cursor: pointer;
        display: none;
    }
    .gwc-box i{
        font-size: 24px;
    }
    .gg-box{
        width: 116px;
        height: 2px;
        background-color: #afafaf;
        position: absolute;
        top: -6px;
        left: 0;
        right: 0;
        margin: 0 auto;
        display: none;
    }
    .ying-box:hover .gg-box,.ying-box:hover .gwc-box,.ying-box:hover .yc-box{
        display: block;
    }
    .h-box img{
        position: absolute;
        left: 0;
        right: 0;
        margin: 0 auto;
        top: -50px;
        z-index: 10;
    }
    .bj-box{
        height: 184px;
        background: url("../../../assets/list/bj7.png") no-repeat;
        background-size: cover;
        position: absolute;
        top:50px;

    }
    .ye-box{
        height: 80px;
        background-color: rgba(255,220,146,.8);
        position: absolute;
        z-index: 20;
        left: 0;
        right: 0;
        bottom: 30px;
        margin: 0 auto;
    }
    .ha-box{
        font-weight: 600;
        font-size: 20px;
        margin-top: 8px;
    }
    .ma-box{
        font-weight: 600;
        margin: 4px 0;
    }
    .en-box{
        font-size: 10px;
    }
    .xia-box{
        height: 34px;
        position: absolute;
        bottom: -10px;
    }
    .er-box{
        font-weight: 600;
        font-size: 24px;
        letter-spacing: 1px;
        line-height: 34px;
    }
    .q-box{
        font-size: 10px;
        text-align: left;
        padding-top: 14px;
        padding-left: 4px;
        box-sizing: border-box;
    }
    .block{
        margin: 20px 0;
    }
    .yz-box1{
        background: url("../../../assets/list/t3.png") no-repeat;
        background-position: center center;
    }
    .yz-box4{
        background: url("../../../assets/list/t4.png") no-repeat;
        background-position: center center;
    }
    .yz-box5{
        background: url("../../../assets/list/t5.png") no-repeat;
        background-position: center center;
    }
    .yz-box6{
        background: url("../../../assets/list/t6.png") no-repeat;
        background-position: center center;
    }
    .yz-box7{
        background: url("../../../assets/list/t7.png") no-repeat;
        background-position: center center;
    }
    .yz-box8{
        background: url("../../../assets/list/t8.png") no-repeat;
        background-position: center center;
    }
    .yz-box9{
        background: url("../../../assets/list/t9.png") no-repeat;
        background-position: center center;
    }
    .yz-box11{
        background: url("../../../assets/list/t11.png") no-repeat;
        background-position: center center;
    }
    .yz-box12{
        background: url("../../../assets/list/t12.png") no-repeat;
        background-position: center center;
    }
    .yz-box13{
        background: url("../../../assets/list/t13.png") no-repeat;
        background-position: center center;
    }
    .yz-box14{
        background: url("../../../assets/list/t14.png") no-repeat;
        background-position: center center;
    }
    .yz-box15{
        background: url("../../../assets/list/t15.png") no-repeat;
        background-position: center center;
    }
    .form-box{
        height: auto!important;
    }
</style>
