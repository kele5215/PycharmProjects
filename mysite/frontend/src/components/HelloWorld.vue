<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h1>
      <router-link to="day01/HelloVue">tiao zhuan zhi HelloVue</router-link>
    </h1>
    <h1>
      <router-link to="day01/Qibu">tiao zhuan zhi Qibu</router-link>
    </h1>
    <h1>
      <router-link to="day02/IfForDemo">tiao zhuan zhi IfForDemo</router-link>
    </h1>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
