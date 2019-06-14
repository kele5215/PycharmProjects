import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import HelloVue from '@/components/day01/HelloWorld'
import Qibu from '@/components/day01/qibu'
import IfForDemo from '@/components/day02/IfForDemo'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/day01/Qibu',
      name: 'Qibu',
      component: Qibu
    },
    {
      path: '/day02/IfForDemo',
      name: 'IfForDemo',
      component: IfForDemo
    },
    {
      path: '/day01/HelloVue',
      name: 'HelloVue',
      component: HelloVue
    }
  ]
})
