import Vue from 'vue'
import Router from 'vue-router'
import MainHeader from '@/components/includes/header/Header'
import Home from '@/components/home/Home'

import listRoutes from './list.js'

Vue.use(Router)

const mainRoutes = [
  {
    // All lists should render here
    path: '/',
    name: 'Home',
    components: {
      header: MainHeader,
      main: Home
    }
  }
]

let allRoutes = mainRoutes.concat(listRoutes())

export default new Router({
  mode: 'history',
  routes: allRoutes
})
