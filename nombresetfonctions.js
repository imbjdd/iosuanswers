/**
 * Tous les exemples passent. J'ai essayé également chaque fonction de manière individuelle. Pas d'anomalie à constater dans l'output.
 */

function parse(owo) {
	return owo.substring(1, owo.length-2).split(',').map(x => x.trim())
}

function quad(uwu) {
	const symboles = parse(uwu)
	let numbers = []

	for(let i = 0; i < symboles.length; i++) {
		let symbole = symboles[i]

		// là c'est un nombre
		if(symbole == parseInt(symbole)) {
			numbers.push(parseInt(symbole))
		}

		else if(symbole.substring(0,6) === 'λn.(n*') {
			let n = symbole.split('*')[1].split(')')[0]
			// je m'assure de bien parse le nombre s'il est mis entre parenthèses
			if(n[0] == '(') n=n.substring(1, n.length)
			for(let j = 0; j < numbers.length; j++) {
				numbers[j] *= parseInt(n)
			}
		}

		else if(symbole.substring(0,6) === 'λn.(n+') {
			let n = symbole.split('+')[1].split(')')[0]
			if(n[0] == '(') n=n.substring(1, n.length)
			for(let j = 0; j < numbers.length; j++) {
				numbers[j] += parseInt(n)
			}
		}

		else if(symbole.substring(0,6) === 'λn.(n-') {
			let n = symbole.split('-').slice(1).join('-').split(')')[0]
			if(n[0] == '(') n=n.substring(1, n.length)
			for(let j = 0; j < numbers.length; j++) {
				numbers[j] -= parseInt(n)
			}
		}

		else if(symbole.substring(0,6) === 'λn.(n<') {
			let n = symbole.split('<')[1].split(')')[0]
			if(n[0] == '(') n=n.substring(1, n.length)
			numbers = numbers.filter(x => x < n)
		}

		else if(symbole.substring(0,6) === 'λn.(n≤') {
			let n = symbole.split('≤')[1].split(')')[0]
			if(n[0] == '(') n=n.substring(1, n.length)
			numbers = numbers.filter(x => x <= n)
		}

		else if(symbole.substring(0,6) === 'λn.(n>') {
			let n = symbole.split('>')[1].split(')')[0]
			if(n[0] == '(') n=n.substring(1, n.length)
			numbers = numbers.filter(x => x > n)
		}

		// mod
		else if(symbole.substring(0,6) === 'λn.(n ') {
			let n = parseInt(symbole.split('mod')[1].split('=')[0])
			let d = parseInt(symbole.split('=')[2].split(')')[0])
			if(d[0] == '(') d=d.substring(1, d.length)
			numbers = numbers.filter(x => x%n === d)
		}

		else if(symbole.substring(0,6) === 'λn.(n≥') {
			let n = symbole.split('≥')[1].split(')')[0]
			if(n[0] == '(') n=n.substring(1, n.length)
			numbers = numbers.filter(x => x >= n)
		}

		else if(symbole.substring(0,6) === 'λn.(-n') {
			for(let j = 0; j < numbers.length; j++) {
				numbers[j] = -numbers[j]
			}
		}
	}
	
	return '[' + numbers.join(',') + ']'
}

function append(ent) {
	fs.appendFileSync('output.txt', ent+'\n')
}

function solution(text) {
	const lines = text.split('\n').slice(0, text.split('\n').length-1)
	for(let i = 0; i < lines.length; i++) {
		append(quad(lines[i]))
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
