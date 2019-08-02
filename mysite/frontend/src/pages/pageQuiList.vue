<template>
  <div id="pageQuiList" class="qui-list">
    <qui-list v-on:listBtnClickEvent="testList"></qui-list>
    <qui-list tipText="自定义文案，默认右边是按钮" msg="弹层"></qui-list>
    <qui-list
      tipText="最右边是箭头"
      currentView="qui-arrow"
      v-on:listBtnClickEvent="testArrow"
    ></qui-list>
  </div>
</template>

<script>
import quiList from '../components/quiList.vue'
export default {
  name: 'pageQuiList',
  components: {
    'qui-list': quiList
  },
  methods: {
    testList: function () {
      alert('wo shi testList')
    },
    testArrow: function () {
      alert('wo shi testArrow')
    }
  }
}
</script>

<style scoped>
</style>
