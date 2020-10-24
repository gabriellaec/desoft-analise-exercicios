with open('macacos-me-mordam.txt','r') as arquivo:
	conteudo = arquivo.read()

contador = 0

for i in range(len(conteudo)):
	if conteudo[i] == "b" or conteudo[i] == "B":
		if conteudo[i+1] == "a" or conteudo[i+1] == "A":
			if conteudo[i+2] == "n" or conteudo[i+2] == "N":
				if conteudo[i+3] == "a" or conteudo[i+3] == "A":
					if conteudo[i+4] == "n" or conteudo[i+4] == "N":
						if conteudo[i+3] == "a" or conteudo[i+3] == "A":
							contador +=1


print(contador)