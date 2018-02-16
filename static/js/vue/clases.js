
new Vue({
   delimiters: ['${', '}'],
   el:"#main",
   methods: {
      createTask: function(){
         this.tasks.push({
            description: this.new_task,
            pending: true,
            editing: false
         });

         this.new_task = '';
      }
   },
   data:{
      new_task: '',
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