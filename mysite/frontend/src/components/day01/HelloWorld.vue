<template>
  <div id="vue">Hello Vue.js!{{ message }}</div>
</template>

<script>
export default {
  name: 'HelloVue',
  data () {
    return {
      message: 'suibian'
    }
  }
}
</script>

<style type="text/css">
#vue {
  color: green;
  font-size: 28px;
}
</style>
