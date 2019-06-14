<template>
  <div id="vue_det">
    <h1>site : {{ site }}</h1>
    <h1>url : {{ url }}</h1>
    <h1>{{ details() }}</h1>
    <h6><div v-html="message"></div></h6>
    <div id="vbind">
      <label for="r1">xiugia yanse </label>
      <input type="checkbox" v-model="isActive" id="r1" />
      <br /><br />
      <div v-bind:class="{ class1: isActive }">v-bind:class 指令</div>
    </div>
    <div id="testJs">
      {{ 5 + 5 }}<br />
      {{ ok ? "yes" : "no" }}<br />
      {{
        message2
          .split("")
          .reverse()
          .join("")
      }}
      <div v-bind:id="{ id: 'list-' + index }">cai niao jiao cheng list-n</div>
    </div>
    <div id="testVif">
      <p v-if="seen">现在你看到我了</p>
    </div>
    <div id="testhref">
      <pre><a v-bind:href="url_self">菜鸟教程</a></pre>
    </div>
    <div id="testInput">
      <p>{{ message3 }}</p>
      <input v-model="message3" />
      <br />
      <p>{{ message4 }}</p>
      <button v-on:click="reverseMsg">反转字符串</button>
      <br />
      <br />
      {{ message5 | capitalize }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'Qibu',
  data () {
    return {
      site: '菜鸟教程',
      url: 'www.runoob.com',
      message: '<h6>菜鸟教程</h6>',
      isActive: true,
      message2: 'abcdefg菜鸟教程',
      ok: true,
      index: 1,
      seen: true,
      url_self: 'http://www.runoob.com',
      message3: 'test shuang xiang bangding',
      message4: 'Runoob!',
      message5: 'sunoob'
    }
  },
  methods: {
    details () {
      return this.site + ' - 学的不仅是技术，更是梦想！'
    },
    reverseMsg () {
      this.message4 = this.message4.split('').reverse().join('')
    }
  },
  filters: {
    capitalize (value) {
      if (!value) return ''
      value = value.toString()
      return value.charAt(0).toUpperCase() + value.slice(1)
    }
  }

}
</script>

<style scoped>
h6 {
  font-size: 20px;
  color: #42b983;
}
.class1 {
  background: #444;
  color: #eee;
}
</style>
