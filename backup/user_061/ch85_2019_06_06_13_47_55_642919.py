with open("macacos-me-mordam.txt", "r", encoding="utf8") as file:
	conteudo = file.read()
    
def encontra_palavra(string, palavra):
	contador = 0
	string  = string.upper()
	palavra = palavra.upper()
	for palavras in string.split():
		if palavra == palavras:
			contador += 1
	return contador

encontra_palavra(conteudo,"banana")