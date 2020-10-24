with open('macacos-me-mordam.txt','r') as arquivo:
	conteudo = arquivo.read()

contador = 0

if "banana" in conteudo or "Banana" in conteudo:
	contador += 1
elif "BANANA" in conteudo or "BaNaNa" in conteudo:
	contador += 1
elif "bAnAnA" in conteudo or "bANANA" in conteudo:
    contador += 1

print(contador)