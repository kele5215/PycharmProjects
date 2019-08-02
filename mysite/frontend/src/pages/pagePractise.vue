<template>
  <div>
    <watch-counter></watch-counter>
    <kilometers-compute></kilometers-compute>
    <shopping-car></shopping-car>
  </div>
</template>

<script>
import watchCounter from '../components/watchCounter.vue'
import kilometersCompute from '../components/kilometersCompute.vue'
import shoppingCar from '../components/shoppingCar.vue'
export default {
  components: {
    'watch-counter': watchCounter,
    'kilometers-compute': kilometersCompute,
    'shopping-car': shoppingCar
  }
}
</script>
