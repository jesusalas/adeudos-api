
var urlUsers = '/rutas';

new Vue({
   delimiters: ['${', '}'],
   el:"#main",
   created: function(){
      this.getUsers();
   },
   data:{
      list:[]
   },
   methods:{
      getUsers: function(){
         axios.get(urlUsers).then(response => {
            this.list = response.data;
         });
      }
   }
});
