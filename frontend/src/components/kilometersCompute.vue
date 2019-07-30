<template>
  <div id="computed_props">
    <div>
      <span class="meters-compute">千米 : </span>
      <input type="text" v-model="kilometers" />
    </div>
    <div>
      <span class="meters-compute">米 : </span>
      <input type="text" v-model="meters" />
    </div>
    <p id="info"></p>
  </div>
</template>

<script>
export default {
  el: '#computed_props',
  data: function () {
    return {
      kilometers: 0,
      meters: 0
    }
  },
  watch: {
    kilometers: {
      handler (newValue, oldValue) {
        // document.getElementById('info').innerHTML = '修改前值为: ' + oldValue + '，修改后值为: ' + newValue
        // this.kilometers = newValue
        this.meters = this.kilometers * 1000
      },
      immediate: true
    },

    meters: {
      handler (newValue, oldValue) {
        this.kilometers = newValue / 1000
        // this.meters = newValue;
      },
      immediate: true
    }
  }
}
</script>

<style scoped>
.meters-compute {
  text-align: right;
}
</style>
