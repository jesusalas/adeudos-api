  new Vue({
    delimiters: ['${', '}'],
    el:"#main",
    created: function(){
      this.getData('rutas');
      this.getData('cedis');
    },
    data: {
        routes_list: [],
        cedis_list: [],
        clients_list: [],
        visits_list: [],
        points_gps_list:[]
    },
    methods:{
      getData(type){
        var urlData = "/" + type;
        this.$http.get(urlData).then(function(response){
            
            switch(type) {
                case "cedis": this.cedis_list = response.data;
                    break;
                case "rutas": this.routes_list = response.data;
                    break;
                case "visitas": this.visits_list = response.data;
                    break;
                case "clientes": this.clients_list = response.data;
                    break;
                case "gps": this.points_gps_list = response.data;
                    break;
                default: return false;
            }
        });
      }
    },
  });
    