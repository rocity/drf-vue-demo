import Vue from 'vue'
import Router from 'vue-router'
import MainHeader from '@/components/includes/header/Header'
import Home from '@/components/home/Home'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Hello',
      components: {
        header: MainHeader,
        main: Home
      }
    }
  ]
})
