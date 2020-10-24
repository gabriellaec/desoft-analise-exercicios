niver={'Nico Uno': '01/01/1992', 'Horácio P. Genaro': '03/03/1992', 'Ukibe Nokome': '05/05/1992', 'Maurício Melo': '07/09/1992', 'Abigail Oliveira': '09/09/1992'}

def aniversariantes_de_setembro(niver):
	sete={}
	for nomes,aniversario in niver.items():
		if aniversario[4]=='0' and aniversario[5]=='9':
			sete[nomes]=aniversario
	return sete