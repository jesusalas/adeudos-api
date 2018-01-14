new Vue({
	delimiters: ['${', '}'],
	el:'#main',
	data: {
		people: ['jesus', 'pedro', 'alejandro', 'daniel']
	},
	name: '',
	methods: {
		addName: function(){
			this.people.push(this.name);
			this.name = '';
		}
	}
});
