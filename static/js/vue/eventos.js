new Vue({
   delimiters: ['${', '}'],
   el:"#main",
   data:{
      people: ['jesus', 'daniel', 'kevin', 'cristina'],
      name:'',
      num:0,
   },
   methods:{
      addName: function () {
         this.people.push(this.name);
         this.name = '';
      }
   }
});