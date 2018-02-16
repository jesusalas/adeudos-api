
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
      },
      toggleStatus: function(task){
         task.pending  = !task.pending;

      },
      editTask: function(task){
         this.tasks.forEach(function(task){
            task.editing = false;
         });
         this.draft = task.description;
         task.editing = true;
      },
      updateTask: function(task){
         task.description = this.draft;
         task.editing = false;
      },
      discardTask: function(task){
         task.editing = false;
      }
   },
   data:{
      draft: '',
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
            editing: false
         },
         {
            description: 'Grabar lección de Vue',
            pending: false,
            editing: false
         }
      ]
   }
});