<template>
  <div id="shoppingList">
    <table>
      <tr>
        <th v-for="colNm in colNm_Json" :key="colNm">{{ colNm }}</th>
      </tr>
      <tr v-for="iphone in iphone_Json" :key="iphone">
        <td>{{ iphone.id }}</td>
        <td>{{ iphone.name }}</td>
        <td>{{ iphone.price }}</td>
        <td>
          <button
            v-bind:disabled="iphone.count === 0"
            v-on:click="iphone.count -= 1"
          >
            -
          </button>
          {{ iphone.count }}
          <button v-on:click="iphone.count += 1">+</button>
        </td>
        <td><button v-on:click="iphone.count = 0">移除</button></td>
      </tr>
    </table>

    <div id="shoppingCount">
      <span>总价：{{ totalPrice(iphone_Json) }}</span>
    </div>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      colNm_Json: ['序号', '商品名称', '商品价格', '购买数量', '操作'],
      iphone_Json: [
        {
          id: 1,
          name: 'iphone 8',
          price: 5099,
          count: 1
        },
        {
          id: 2,
          name: 'iphone xs',
          price: 8699,
          count: 1
        },
        {
          id: 3,
          name: 'iphone xr',
          price: 6499,
          count: 1
        },
        {
          id: 4,
          name: 'iphone xs max',
          price: 10299,
          count: 1
        }
      ]
    }
  },
  methods: {
    totalPrice: function (items) {
      var totalP = 0
      items.forEach(element => {
        totalP += element.price * element.count
      })
      return totalP
    }
  }
}
</script>

<style scoped>
table {
  border: 1px solid black;
}
table {
  width: 100%;
}

th {
  height: 50px;
}
th,
td {
  border-bottom: 1px solid #ddd;
}
</style>
