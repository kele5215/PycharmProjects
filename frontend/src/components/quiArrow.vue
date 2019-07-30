<template>
  <a class="qui-arrow" :href="getHref()">❯</a>
</template>

<script>
export default {
  methods: {
    getHref: function () {
      return 'https://translate.google.com/?hl=ja'
    }
  }
}
</script>

<style scoped>
.qui-arrow {
  font-size: 18px;
  color: #aaa;
  margin-right: 10px;
}
</style>
