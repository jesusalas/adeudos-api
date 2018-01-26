
var urlUsers = 'https://randomuser.me/api/?results=10';

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
         this.$http.get(urlUsers).then(function(response){
            this.list = response.data.results;
         });
      }
   }
});
