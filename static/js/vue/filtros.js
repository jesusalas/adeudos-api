
new Vue({
   delimiters: ['${', '}'],
   el:"#main",
   data:{
         list:[],
         name:'',
   },
   methods:{
         getRoutes: function(){
            axios.get("/rutas").then(response => {
               this.list = response.data
            });
         }
    },
    computed:{
      searchRoute: function(){
         return this.list.filter((item)=> item.route.includes(this.name));
      }
    }
});