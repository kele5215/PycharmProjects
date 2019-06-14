<template>
  <div>
    <p>{{ message }}</p>
    <br /><br />
    <div id="testIfFor">
      <div v-if="Math.random() > 0.5">
        Now you see me
      </div>
      <div v-else>
        Now you don't
      </div>
      <br /><br />
      <div v-if="type === 'A'">
        A
      </div>
      <div v-else-if="type === 'B'">
        B
      </div>
      <div v-else-if="type === 'C'">
        C
      </div>
      <div v-else>
        Not A/B/C
      </div>
      <br /><br />
      <div id="forTest">
        <ul>
          <li v-for="site in sites" :key="site.id">
            {{ site.name }}<br />
            --------------
          </li>
        </ul>
        <p>------------------------------------</p>
        <ul>
          <!-- <li v-for="value in object" :key="value.name">{{ value }}</li> -->
          <!-- <li v-for="(value, key) in object" :key="value.name">
            {{ key }}:{{ value }}
          </li> -->
          <li v-for="(value, key, index) in object" :key="value.name">
            {{ index }}.{{ key }}:{{ value }}
          </li>
        </ul>
        <p>------------------------------------</p>
        <ul>
          <li v-for="n in 10" :key="n">
            {{ n }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      message: 'If_for_Demo',
      type: 'D',
      sites: [
        { name: 'tian' },
        { name: 'wu' },
        { name: 'zhang' }
      ],
      object: {
        name: '菜鸟教程',
        url: 'http://www.runoob.com',
        slogan: '学的不仅是技术，更是梦想！'
      }
    }
  }
}
</script>

<style scoped>
</style>
