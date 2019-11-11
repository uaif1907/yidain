import Vue from 'vue'
import App from './App.vue'
import router from './router/router'
import ElementUI from 'element-ui';
import VCharts from 'v-charts'
import 'element-ui/lib/theme-chalk/index.css';
import echarts from 'echarts'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)

Vue.prototype.$echarts = echarts

Vue.config.productionTip = false
Vue.use(ElementUI);
Vue.use(VCharts);

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
