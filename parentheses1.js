function isValid(line) {
	const par = []

	for(let i = 0; i < line.length; i++) {
		if(line[i] === ')') {
			if(par.length === 0) return false
			par.pop()
		}
		else {
			par.push(line[i])
		}
	}

	return par.length === 0
}
pop = 0
function append(ent) {
	pop++
	fs.appendFileSync('output.txt', ent+'\n')
}
	
function solution(text) {
	const lines = text.split('\n').slice(0, text.split('\n').length-1)
	console.log(lines.length)
	for(let i = 0; i < lines.length; i++) {
		const plop = isValid(lines[i])
		append(plop?'True':'False')
	}
}



const fs = require('fs')
function getFile() {
	fs.readFile('input.txt', 'utf8', (err, data) => {
  		if (err) throw err;
  		solution(data)
	});
}

getFile()
