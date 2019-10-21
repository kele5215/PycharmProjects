/* exports 和 module.exports 的使用

 如果要对外暴露属性或方法，
 就用 exports 就行，要暴露对象(类似class，
 包含了很多属性和方法)，就用 module.exports。*/
module.exports = {
  title: 'Vue myAdim Template',

  /**
   * @type {boolean} true | false
   * @description Whether fix the header
   */
  fixedHeader: false,

  /**
 * @type {boolean} true | false
 * @description Whether show the logo in sidebar
 */
  sidebarLogo: false
}