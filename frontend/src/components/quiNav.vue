<template>
  <div class="qui-nav nav-type-3">
    <a
      v-for="(item, index) in items"
      :key="(item, index)"
      :class="[commonClass, item.active ? activeClass : '']"
      v-on:click="navClickEvent(items, index)"
    >
      <span class="nav-txt">{{ item.text }}</span>
    </a>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      commonClass: 'nav-item',
      activeClass: 'active',
      items: [
        {
          text: '首页',
          active: true
        },
        {
          text: '列表',
          active: false
        },
        {
          text: '关于',
          active: false
        },
        {
          text: '招聘',
          active: false
        }
      ]
    }
  },
  methods: {
    navClickEvent: function (items, index) {
      items.forEach(element => {
        element.active = false
      })
      items[index].active = true
      this.$emit('navClickEvent', items, index)
    }
  }
}
</script>

<style scoped>
@import "./css/reset.import.css";
@import "./css/qui-nav.import.css";
</style>
