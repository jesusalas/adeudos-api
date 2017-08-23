//Vue.config.delimiters = ["${", "}"];
      //var urlUsers= 'https://randomuser.me/api/?results=5000';
      var urlUsers= '/rutas';
      new Vue({
        delimiters: ['${', '}'],
        el:"#app",
        created: function(){
          this.getUsers();
        },
        data: {
            name: "jesus",
            gender:"h",
            years_php:0,
            lists:[]
        },
        methods:{
          singUp:function (logout, event) {

            event.preventDefault();
            alert(this.name + "por favor espera mientras te registramos");

            if (logout) {
              alert("saliendo del sistema ...");
            }  
          },
          getUsers: function(){
            this.$http.get(urlUsers).then(function(response){
                this.lists = response.data;
            });
          }
        },
      });