<template>
  <div id="shoppingList">
    <table>
      <tr v-for="colNm in colNm_Json" :key="colNm">
        <th>{{ colNm }}</th>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      colNm_Json: ['序号', '商品名称', '商品价格', '购买数量', '操作']
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
