<template>
  <div id="bookCrud">
    <div id="bookNmAdd">
      <input
        v-model="bookNmInput"
        placeholder="请输入书名"
        style="display:inline-table; width: 30%; float:left"
      />
      <button
        type="primary"
        @click="addBook()"
        style="float:left; margin: 2px;"
      >
        新增
      </button>
    </div>
    <div id="bookNmShow">
      <table>
        <tr>
          <th v-for="colNm in colNm_Json" :key="colNm">{{ colNm }}</th>
        </tr>
        <tr v-for="book in bookList_Json" :key="book">
          <td>{{ book.id }}</td>
          <td>{{ book.book_name }}</td>
          <td>{{ book.add_time }}</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'bookNmCrue',
  data: function () {
    return {
      bookNmInput: '',
      colNm_Json: ['编号', '书名', '添加时间'],
      bookList_Json: [
        {
          id: 1,
          book_name: 'iphone 8',
          add_time: 5099
        },
        {
          id: 2,
          book_name: 'iphone xs',
          add_time: 8699

        },
        {
          id: 3,
          book_name: 'iphone xr',
          add_time: 6499

        },
        {
          id: 4,
          book_name: 'iphone xs max',
          add_time: 10299
        }
      ]
    }
  },

  mounted: function () {
    this.showBooks()
  },

  methods: {
    addBook () {
      this.$axios.get('http://127.0.0.1:8000/api/add_book?book_name=' + this.bookNmInput)
        .then((response) => {
          var res = response.data
          if (res.error_num === 0) {
            this.showBooks()
          } else {
            // this.$message.error('新增书籍失败，请重试')
            console.log(res['msg'])
          }
        })
    },
    showBooks () {
      this.$axios.get('http://127.0.0.1:8000/api/show_books')
        .then((response) => {
          // var res = response
          console.log(response)
          if (response.data.error_num === 0) {
            this.bookList_Json = response['list']
          } else {
            // this.$message.error('查询书籍失败')
            console.log(response['msg'])
          }
        })
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
  background: yellowgreen;
  height: 50px;
}

td {
  border-bottom: 1px solid #ddd;
}
</style>
