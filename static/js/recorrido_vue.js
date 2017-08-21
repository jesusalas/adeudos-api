  
  var urlRoutes= '/rutas';
    new Vue({
      delimiters: ['${', '}'],
      el:"#routes",
      created: function(){
        this.getRoutes();
      },
      data: {
          routes_list:[]
      },
      methods:{
        getRoutes: function(){
          this.$http.get(urlRoutes).then(function(response){
              this.routes_list = response.data;
          });
        }
      },
    });

  var urlCedis = "/cedis";
    new Vue({
      delimiters: ['${', '}'],
      el:"#cedis",
      created: function(){
        this.getCedis();
      },
      data: {
          cedis_list:[]
      },
      methods:{
        getCedis: function(){
          this.$http.get(urlCedis).then(function(response){
              this.cedis_list = response.data;
          });
        }
      },
    });

  var urlClients = "/clientes";
    new Vue({
      delimiters: ['${', '}'],
      el:"#clientes",
      created: function(){
        this.getClients();
      },
      data: {
          clients_list:[]
      },
      methods:{
        getClients: function(){
          this.$http.get(urlClients).then(function(response){
              this.clients_list = response.data;
          });
        }
      },
    });

  var urlVisits = "/visitas";
    new Vue({
      delimiters: ['${', '}'],
      el:"#visitas",
      created: function(){
        this.getVisits();
      },
      data: {
          visits_list:[]
      },
      methods:{
        getVisits: function(){
          this.$http.get(urlVisits).then(function(response){
              this.visits_list = response.data;
          });
        }
      },
    });

  var urlPointsGps = "/gps";
  new Vue({
    delimiters: ['${', '}'],
    el:"#gps",
    created: function(){
      this.getPointsGps();
    },
    data: {
        points_gps_list:[]
    },
    methods:{
      getPointsGps: function(){
        this.$http.get(urlPointsGps).then(function(response){
            this.points_gps_list = response.data;
        });
      }
    },
  });