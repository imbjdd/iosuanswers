function gen(i) {
	if(i === 0) return []
	if(i === 1) return ['()']
	const av = gen(i-1)
	const sol = []
	for(let i = 0; i < av.length; i++) {
		const el = av[i]
		let z = '('+el+')'
		if(!sol.includes(z)) sol.push(z)
		let y = '()' + el
		if(!sol.includes(y)) sol.push(y)
		let x = el + '()'
		if(!sol.includes(x)) sol.push(x)

	}
	return sol.sort()
}

pop = 0
function append(ent) {
	pop++
	fs.appendFileSync('output.txt', ent+'\n')
}


function solution(text) {
	const numbers = text.split('\n').slice(0, text.split('\n').length-1).map(x => parseInt(x))
	for(let i = 0; i < numbers.length; i++) {
		append(gen(numbers[i]))
	}
}

const fs = require('fs')
function getFile() {
	fs.readFile('28601935.txt', 'utf8', (err, data) => {
  		if (err) throw err;
  		solution(data)
	});
}

getFile()
