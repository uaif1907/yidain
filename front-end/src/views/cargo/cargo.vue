<template>
    <div class="cargo-box">
        <!--        上-->
        <el-row :span="24" style="margin-bottom: 20px">
            <el-col :span="8" style="background-color: white;padding: 0 10px">
                <div class="size">
                    <span></span>
                    <h4>已上架类目</h4>
                    <span></span>
                </div>
                <div class="block">
                    <span class="demonstration">座椅</span>
                    <el-slider v-model="value1" :show-tooltip="false" class="hua"></el-slider>
                    <div class="you">
                        <p>60%</p>
                        <p>2453件</p>
                    </div>
                </div>
                <div class="block">
                    <span class="demonstration">沙发</span>
                    <el-slider v-model="value2" :show-tooltip="false" class="sf"></el-slider>
                    <div class="you">
                        <p>40%</p>
                        <p>2110件</p>
                    </div>
                </div>
                <div class="block">
                    <span class="demonstration">床具</span>
                    <el-slider v-model="value3" :show-tooltip="false" class="cj"></el-slider>
                    <div class="you">
                        <p>40%</p>
                        <p>2110件</p>
                    </div>
                </div>
                <div class="block">
                    <span class="demonstration">灯具</span>
                    <el-slider v-model="value4" :show-tooltip="false" class="dj"></el-slider>
                    <div class="you">
                        <p>70%</p>
                        <p>2643件</p>
                    </div>
                </div>
                <div class="block">
                    <span class="demonstration">柜具</span>
                    <el-slider v-model="value5" :show-tooltip="false" class="gj"></el-slider>
                    <div class="you">
                        <p>70%</p>
                        <p>2643件</p>
                    </div>
                </div>
            </el-col>
            <el-col :span="8" style="background-color: white;height: 280px">
                <div>
                    <div class="size">
                        <span></span>
                        <h4>订单统计量</h4>
                        <span></span>
                    </div>
                    <ve-histogram :data="zhuData" :settings="zhuSettings" :legend="legend" :colors="color" :tooltip="{trigger:'item'}" height="281px" :series="series" :yAxis="yAxis"></ve-histogram>
                </div>
            </el-col>
            <el-col :span="8" style="background-color: white;height: 280px">
                <div>
                    <div class="size">
                        <span></span>
                        <h4>余量</h4>
                        <span></span>
                    </div>
                    <ve-histogram :data="zhuData" :settings="zhuSettings" :legend="legend" :colors="colors" :tooltip="{trigger:'item'}" height="281px" :series="series" :yAxis="yAxis"></ve-histogram>
                </div>
            </el-col>
        </el-row>
        <!--下-->
        <!--        表格-->
        <el-row :span="24">
            <div class="s-box">
                <div class="size">
                    <span></span>
                    <h4>货物列表</h4>
                    <span></span>
                </div>
                <div class="xz" @click="add=true">
                    <i class="el-icon-circle-plus"></i>
                    <h4>新增货物</h4>
                </div>
            </div>
            <el-table :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))" style="width: 100%">
                <el-table-column label="ID" prop="id" width="50"></el-table-column>
                <el-table-column label="商品图片" width="200">
                    <el-image
                            style="width: 100px; height: 100px"
                            :src="url"
                            :preview-src-list="srcList"
                            prop="order">
                    </el-image>
                </el-table-column>
                <el-table-column label="商品名称" prop="consumer" width="100"></el-table-column>
                <el-table-column label="价格" prop="phone" width="120"></el-table-column>
                <el-table-column label="描述" prop="area"></el-table-column>
                <el-table-column label="款式" prop="monetary" width="80"></el-table-column>
                <el-table-column align="right" label="操作" style="display: flex">
                    <template slot-scope="scope">
                        <el-button size="mini" style="background: -webkit-linear-gradient(left,#ff6969,#ff6969);color: white" @click="handleDelete(scope.$index)">删除</el-button>
                        <el-button size="mini" style="background: -webkit-linear-gradient(left,#67c1fd,#71dcfd);color: white" @click="changeform(scope.$index,scope.row)">修改</el-button>
                    </template>

                </el-table-column>
            </el-table>

        </el-row>
        <!-- 新增-->
        <el-dialog title="新增商品" :visible.sync="add">
            <el-form :model="form">
                <el-row :span="24" style="display: flex;justify-content: space-around">
                    <el-col :span="4">
                        <div>
                            <span>商品图</span>
                            <el-upload
                                    action="https://jsonplaceholder.typicode.com/posts/"
                                    list-type="picture-card"
                                    :on-preview="handlePictureCardPreview"
                                    :on-remove="handleRemove"
                                    v-model="form.order">
                                <i class="el-icon-plus"></i>
                            </el-upload>
                            <el-dialog :visible.sync="dialogVisible">
                                <img width="100%" :src="dialogImageUrl" alt="">
                            </el-dialog>
                        </div>
                    </el-col>
                    <el-col :span="4">
                        <div>
                            <span>商品名称</span>
                            <el-input v-model="form.consumer" autocomplete="off" style="margin-top: 30px"></el-input>
                        </div>
                    </el-col>
                    <el-col :span="4">
                        <div>
                            <span>价格</span>
                            <el-input v-model="form.phone" autocomplete="off" style="margin-top: 30px"></el-input>
                        </div>
                    </el-col>
                    <el-col :span="4">
                        <div>
                            <span>描述</span>
                            <el-input v-model="form.area" autocomplete="off" style="margin-top: 30px"></el-input>
                        </div>
                    </el-col>
                    <el-col :span="4">
                        <div>
                            <span>款式</span>
                            <el-input v-model="form.monetary" autocomplete="off" style="margin-top: 30px"></el-input>
                        </div>
                    </el-col>
                </el-row>

            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="add = false">取 消</el-button>
                <el-button type="primary" @click="addform(form)">确 定</el-button>
            </div>
        </el-dialog>
        <!-- 修改-->
        <el-dialog title="修改商品" :visible.sync="change">
            <el-form :model="editRegisterData">
                <el-row :span="24" style="display: flex;justify-content: space-around">
                    <el-col :span="4">
                        <div>
                            <span>商品图</span>
                            <el-image
                                    style="width: 100px; height: 100px"
                                    :src="url"
                                    :preview-src-list="srcList"
                                    prop="editRegisterData.order">
                            </el-image>
                        </div>
                    </el-col>
                    <el-col :span="4">
                        <div>
                            <span>商品名称</span>
                            <el-input v-model="editRegisterData.consumer" autocomplete="off" style="margin-top: 30px"></el-input>
                        </div>
                    </el-col>
                    <el-col :span="4">
                        <div>
                            <span>价格</span>
                            <el-input v-model="editRegisterData.phone" autocomplete="off" style="margin-top: 30px"></el-input>
                        </div>
                    </el-col>
                    <el-col :span="4">
                        <div>
                            <span>描述</span>
                            <el-input v-model="editRegisterData.area" autocomplete="off" style="margin-top: 30px"></el-input>
                        </div>
                    </el-col>
                    <el-col :span="4">
                        <div>
                            <span>款式</span>
                            <el-input v-model="editRegisterData.monetary" autocomplete="off" style="margin-top: 30px"></el-input>
                        </div>
                    </el-col>
                </el-row>

            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="change = false">取 消</el-button>
                <el-button type="primary" @click="changetj()">确 定</el-button>
            </div>
        </el-dialog>

    </div>
</template>

<script>
    export default {
        name: 'Cargo',
        props: {
            // msg: String
        },
        data(){
            this.zhuSettings = {
                metrics: ['订单量'],
                dimension: ['类别'],
            };
            return {

                editRegisterData:{},
                change:false,
                dialogImageUrl: '',
                dialogVisible: false,//图片
                formLabelWidth: '120px',
                form:{},//添加
                add:false,
                dialogFormVisible: false,
                formDate:{},
                search: '',
                value1:60,
                value2:40,
                value3:40,
                value4:70,
                value5:70,
                color:['#65bbfc','#da87ec','#e26172'],
                colors:['#da87ec'],
                legend:{
                    right:30,top:10,bottom:10
                },
                series:[
                    {
                        type:'bar',
                        barWidth: '30%',
                        data:[160, 260, 164, 300, 230, 180],
                        itemStyle: {
                            barBorderRadius: [50, 50, 0, 0],
                        }
                    }

                ],
                yAxis:[
                    {
                        name:'订单量/件',
                    }
                ],
                zhuData: {

                    columns: ['类别', '订单量'],
                    rows: [
                        { '类别': '座椅', '订单量': 393, },
                        { '类别': '沙发', '订单量': 930, },
                        { '类别': '床具', '订单量': 423, },
                        { '类别': '灯具', '订单量': 723, },
                        { '类别': '柜具', '订单量': 192, },
                    ]
                },
                tableData: [{
                    id:1,
                    order:'',
                    consumer:'ADE-阿德',
                    phone:'￥269.0',
                    area:'采用曲木设计，结实耐用，十分灵活，占用面积小',
                    monetary:"经典款",
                    pay:0,
                    state:6,
                    ordertime:'2019-05-25 9:00',
                },
                {
                    id:2,
                    order:'',
                    consumer:'ADE-德',
                    phone:'￥269.0',
                    area:'采用曲木设计，结实耐用，十分灵活，占用面积小',
                    monetary:"经典款",
                    pay:0,
                    state:6,
                    ordertime:'2019-05-25 9:00',
                },
                {
                    id:3,
                    order:'',
                    consumer:'ADE-阿',
                    phone:'￥269.0',
                    area:'采用曲木设计，结实耐用，十分灵活，占用面积小',
                    monetary:"经典款",
                    pay:0,
                    state:6,
                    ordertime:'2019-05-25 9:00',
                }],
                url: 'https://img.alicdn.com/bao/uploaded/i3/2262300335/O1CN019fEmXK1ELTDgkTz8b_!!0-item_pic.jpg',
                srcList: [
                    'https://img.alicdn.com/bao/uploaded/i3/2262300335/O1CN019fEmXK1ELTDgkTz8b_!!0-item_pic.jpg',
                    'https://img.alicdn.com/bao/uploaded/i3/2262300335/O1CN019fEmXK1ELTDgkTz8b_!!0-item_pic.jpg'
                ],
            }
        },
        methods: {
            handleSelect() {
            },
            handleClose() {
            },

            handleRemove() {
            },
            handlePictureCardPreview(file) {
                this.dialogImageUrl = file.url;
                this.dialogVisible = true;
            },
            //添加
            addform(data){
                this.add = false;
                this.tableData.push(data)
            },
            // 修改
            changeform(index,row){
                this.change = true;
                this.editRegisterData = JSON.parse(JSON.stringify(row));
                this.tableData[index]=this.editRegisterData;
            },
            changetj(){
                this.change = false;
            },
            //删除
            handleDelete(index) {
                this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    this.tableData.splice(index,1);
                    this.$message({
                        type: 'success',
                        message: '删除成功!'
                    });
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消删除'
                    });
                });
            },
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .block{
        display: flex;
        margin: 10px 0;
    }
    .block span{
        line-height: 38px;
    }
    .sf{
        width: 260px;
        margin: 0 8px
    }
    .cj{
        width: 260px;
        margin: 0 8px
    }
    .dj{
        width: 260px;
        margin: 0 8px
    }
    .gj{
        width: 260px;
        margin: 0 8px
    }
    .hua{
        width: 260px;
        margin: 0 8px
    }
    .you{
        height: 38px;
        text-align: left;
    }
    .you p{
        font-size: 14px;
        color: #8c8c8c;
    }
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
    .xz h4{
        line-height: 40px;
        font-weight: 400;
    }

</style>
