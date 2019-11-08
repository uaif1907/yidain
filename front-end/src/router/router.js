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
        path: 'chair',
        name: 'chair',// 座椅页
        component: () => import('../views/front-page/Chair.vue'),

      },
      {
        path: 'bed',
        name: 'bed',// 床页
        component: () => import('../views/front-page/Bed.vue'),

      },
      {
        path: 'cabinet',
        name: 'cabinet',// 柜子页
        component: () => import('../views/front-page/Cabinet.vue'),

      },
      {
        path: 'edge',
        name: 'edge',// 边几页
        component: () => import('../views/front-page/Edge.vue'),

      },
      {
        path: 'person',
        name: 'person',// 个人中心页
        component: () => import('../views/front-page/Person.vue'),
        children:[
          {
            path:'one',
            name:'one',
            component:() => import('../components/front-end/person/one.vue')
          },
          {
            path:'two',
            name:'two',
            component:() => import('../components/front-end/person/two.vue')
          },
          {
            path:'three',
            name:'three',
            component:() => import('../components/front-end/person/three.vue')
          },

        ]

      },
      {
        path: 'shopcar',
        name: 'shopcar',// 购物车页
        component: () => import('../views/front-page/ShopCar.vue'),

      },
    ]
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
