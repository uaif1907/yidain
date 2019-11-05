import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
  {
<<<<<<< HEAD
    path:'/',
    name:'',
    
=======
    path: '/',
    name: '', // 头和尾
    component: () => import('../views/front-page/Basis.vue'),
    redirect: '/first' ,
    children: [
      {
        path: 'first',
        name: 'first',// 首页
        component: () => import('../views/front-page/First.vue'),

      },
      {
        path: 'details',
        name: 'details',// 详情页
        component: () => import('../views/front-page/Details.vue'),

      },
      {
        path: 'login',
        name: 'login',// 登录页
        component: () => import('../views/front-page/Login.vue'),

      },
      {
        path: 'list',
        name: 'list',// 列表页
        component: () => import('../views/front-page/List.vue'),

      },
      {
        path: 'person',
        name: 'person',// 个人中心页
        component: () => import('../views/front-page/Person.vue'),

      },
      {
        path: 'shopcar',
        name: 'shopcar',// 个人中心页
        component: () => import('../views/front-page/ShopCar.vue'),

      },
    ]

>>>>>>> 053d18ad120a27e397b693d947bbea9434422606
  },


  // 以下是后台
  {
    path: '/index',
    name: 'index',
    component: () => import('../views/index/index.vue'),
    children: [
      {
        path: 'home',
        name: 'home',
        component: () => import('../views/home/home.vue'),
      },
      {
        path: 'order',
        name: 'order',
        component: () => import('../views/order/order.vue'),
        // children:[

        // ]
      },
      {
        path: 'paid',
        name: 'paid',
        component: () => import('../views/paid/paid.vue'),
      },
      {
        path: 'unpaid',
        name: 'unpaid',
        component: () => import('../views/unpaid/unpaid.vue'),
      },
      {
        path: 'cargo',
        name: 'cargo',
        component: () => import('../views/cargo/cargo.vue'),
        // children:[
        //
        // ]
      },
      {
        path: 'ground',
        name: 'ground',
        component: () => import('../views/ground/ground.vue')
      },
      {
        path: 'notground',
        name: 'notground',
        component: () => import('../views/notground/notground.vue')
      },
      {
        path: 'user',
        name: 'user',
        component: () => import('../views/user/user.vue'),
      },
      {
        path: 'datam',
        name: 'datam',
        component: () => import('../views/datam/datam.vue'),
      }
    ]
  },


];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
