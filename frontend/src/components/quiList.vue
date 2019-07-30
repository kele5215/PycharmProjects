<template>
  <div class="qui-list">
    <span class="list-tips">{{ tipText }}</span>
    <!-- <qui-btn
      v-on:btnClickEvent="listBtnClickEvent"
      :msg="msg"
      class="small"
    ></qui-btn> -->
    <component
      :is="currentView"
      v-on:btnClickEvent="listBtnClickEvent"
      :msg="msg"
      class="small"
    ></component>
  </div>
</template>

<script>
import quiButton from '../components/quiButton'
import quiArrow from '../components/quiArrow'
export default {
  props: {
    msg: {
      default: '下载'
    },
    tipText: {
      default: '默认的文案'
    },
    currentView: {
      default: 'qui-btn'
    },
    btnClickEvent: {
      type: Function,
      default: function () {
        alert(this.msg + '我是默认事件')
      }
    }
  },
  components: {
    'qui-btn': quiButton,
    'qui-arrow': quiArrow
  },
  methods: {
    listBtnClickEvent: function () {
      this.btnClickEvent()
      this.$emit('listBtnClickEvent')
    }
  }
}
</script>

<style scoped>
.qui-list {
  padding: 10px 0;
  margin-left: 10px;
  overflow: hidden;
  border-bottom: 1px solid #e0e0e0;
  vertical-align: middle;
  display: flex;
  justify-content: center;
  align-items: Center;
  min-height: 30px;
}
.qui-list .qui-btn {
  float: right;
  margin-right: 10px;
}
.qui-list .list-tips {
  padding: 0 5px;
  color: #00a0d8;
  float: left;
  vertical-align: middle;
  flex: 1;
  text-align: left;
  font-size: 14px;
}
</style>
