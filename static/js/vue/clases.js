
new Vue({
   delimiters: ['${', '}'],
   el:"#main",
   data:{
      isActive: false,
      tasks: [
         {
            description: 'Aprender Vue.js',
            pending: true,
            editing: false
         },
         {
            description: 'Suscribirse a Styde.net',
            pending: true,
            editing: true
         },
         {
            description: 'Grabar lección de Vue',
            pending: false,
            editing: false
         }
      ]
   }
});