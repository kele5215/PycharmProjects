<template>
  <div id="pageQuiButton">
    <!--使用-->
    <qui-btn class="small"></qui-btn>
    <qui-btn v-on:btnClickEvent="doSth1" msg="确定" class="small"></qui-btn>
    <qui-btn v-on:btnClickEvent="doSth2" msg="下载" class="small">
      <img slot="icon" class="ico" src="../assets/logo.png" />
    </qui-btn>
  </div>
</template>

<script>
import quiBtn from '../components/quiButton.vue'
export default {
  name: 'pageQuiButton',
  components: {
    'qui-btn': quiBtn
  },
  methods: {
    doSth1: function () {
      alert('你点击了组件的click:确定')
    },
    doSth2: function () {
      alert('你点击了组件的click:取消')
    }
  }
}
</script>
