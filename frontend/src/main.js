// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from './axios'// 通过import引入

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app', /* 定义作用范围就是index.html里的id为app的范围内 */
  router, /* 引入路由 */
  axios, // 通过import引入，然后在这里调用
  components: { App }, /* 注册引入的组件App.vue */
  template: '<App/>' /* 给Vue实例初始一个App组件作为template 相当于默认组件 */

})
