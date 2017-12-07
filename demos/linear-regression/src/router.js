import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App'
import Guest from './Guest'
import Auth from './Auth'

Vue.use(VueRouter)

export default new VueRouter({
  routes: [
    {
      path: '/',
      component: App
    },
    {
      path: '/Guest',
      component: Guest
    },
    {
      path: '/Auth',
      component: Auth
    }
  ]
})

