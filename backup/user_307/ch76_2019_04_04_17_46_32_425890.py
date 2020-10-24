niver={}

def aniversariantes_de_setembro(niver):
	sete={}
	for e in niver.values():
		if e[4]=='0' and e[5]=='7':
			sete[e]=e.value()
	return sete