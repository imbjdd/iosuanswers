function uwu(line) {
	const par = []

	let k = 0

	for(let i = 0; i < line.length; i++) {
		if(line[i] === ')') {
			if(par.length === 0) {
				k++
				par.push('(')
			}
			else par.pop()
		}
		else {
			par.push(line[i])
		}
	}

	if(par.length%2!==0) return -1
	k += par.length/2
	return k
}

pop = 0
function append(ent) {
	pop++
	fs.appendFileSync('output.txt', ent+'\n')
}

function solution(text) {
	const lines = text.split('\n').slice(0, text.split('\n').length-1)
	for(let i = 0; i < lines.length; i++) {
		append(uwu(lines[i]))
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
