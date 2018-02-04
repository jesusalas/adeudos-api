
Vue.component('common-list',{
   props: ['list'],
   template: `<ul class="list-group">
                  <li v-for="item in list" class="list-group-item">
                     {{ item.name }}
                  </li>
               </ul>`
});

var urlClients = "/clientes";
var urlCedis = "/cedis";

new Vue({
   delimiters: ['${', '}'],
   el:"#main",
   created: function(){
      this.getClients(),
      this.getCedis()
   },
   data:{
      clients: [],
      cedis: [],
   },
   methods:{
      getClients: function(){
         axios.get(urlClients).then(response => {
            this.clients = response.data;
         });
      },
      getCedis: function(){
         axios.get(urlCedis).then(response => {
            this.cedis = response.data;
         });
      }

   }
});