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
          <td>{{ book.pk }}</td>
          <td>{{ book.fields.book_name }}</td>
          <td>{{ book.fields.add_time }}</td>
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
        // {
        //   id: 1,
        //   book_name: 'iphone 8',
        //   add_time: 5099
        // },
        // {
        //   id: 2,
        //   book_name: 'iphone xs',
        //   add_time: 8699

        // },
        // {
        //   id: 3,
        //   book_name: 'iphone xr',
        //   add_time: 6499

        // },
        // {
        //   id: 4,
        //   book_name: 'iphone xs max',
        //   add_time: 10299
        // }
      ]
    }
  },

  methods: {
    // showBooks: function () {
    //   this.$http.get('http://127.0.0.1:8000/api/show_books')
    //     .then(function (response) {
    //       console.log(response)
    //       var res = response.data
    //       if (res.error_num === 0) {
    //         // this.bookList_Json = response['list']
    //         console.log(res.msg)
    //       } else {
    //         // this.$message.error('查询书籍失败')
    //         console.log(res.msg)
    //       }
    //     })
    //     .catch(error => console.log(error))
    //   console.log('function showBooks')
    // },
    showBooks: function (_self) {
      // var _self = this
      _self.$http.get('http://127.0.0.1:8000/api/show_books')
        .then((response) => {
          console.log(response)
          var res = response.data
          if (res.error_num === 0) {
            _self.bookList_Json = res.list
            console.log(res.msg)
          } else {
            // this.$message.error('查询书籍失败')
            console.log(res.msg)
          }
        })
        .catch(error => console.log(error))
    },
    addBook: function () {
      // var _self = this
      this.$http.get('http://127.0.0.1:8000/api/add_book?book_name=' + this.bookNmInput)
        // .then(function (response) {
        .then((response) => {
          console.log(response)
          var res = response.data
          if (res.error_num === 0) {
            console.log(res.msg)
            this.$options.methods.showBooks(this)
          } else {
            // this.$message.error('新增书籍失败，请重试')
            console.log(res.msg)
          }
        })
        .catch(error => console.log(error))
    }
  },

  mounted: function () {
    this.$options.methods.showBooks(this)
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
