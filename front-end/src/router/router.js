import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  // {
  //   path: '/',
  //   name: 'home',
  //   component: Home
  // },
  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
  {
    path:'/',
    name:'',

  },
  {
    path:'/index',
    name:'index',
    component:() => import('../views/index/index.vue'),
    children: [
      {
        path:'home',
        name:'home',
        component:() => import('../views/home/home.vue'),
      },
      {
        path:'order',
        name:'order',
        component:() => import('../views/order/order.vue'),
        // children:[

        // ]
      },
      {
        path:'paid',
        name:'paid',
        component:() => import('../views/paid/paid.vue'),
      },
      {
        path:'unpaid',
        name:'unpaid',
        component:() => import('../views/unpaid/unpaid.vue'),
      },
      {
        path:'cargo',
        name:'cargo',
        component:() => import('../views/cargo/cargo.vue'),
        // children:[
        //
        // ]
      },
      {
        path:'ground',
        name:'ground',
        component:() => import('../views/ground/ground.vue')
      },
      {
        path:'notground',
        name:'notground',
        component:() => import('../views/notground/notground.vue')
      },
      {
        path:'user',
        name:'user',
        component:() => import('../views/user/user.vue'),
      },
      {
        path:'datam',
        name:'datam',
        component:() => import('../views/datam/datam.vue'),
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
