<template>
  <div id="watchCouter">
    <p class="watchCouter-font">计数器: {{ counter }}</p>
    <button class="watchCouter-font" v-on:click="counter++">
      点我
    </button>
    <p id="watchCouterContent"></p>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      counter: 1
    }
  },
  watch: {
    counter: function (nval, oval) {
      // alert('计数器值的变化 :' + oval + ' 变为 ' + nval + '!')
      document.getElementById('watchCouterContent').innerHTML = '计数器值的变化 :' + oval + ' 变为 ' + nval + '!'
    }
  }
}
</script>

<style scoped>
.watchCouter-font {
  font-size: 25px;
}
</style>
