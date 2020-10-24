with open("macacos-me-mordam.txt", "r") as arquivo:
    conteudo = arquivo.read()
contador = 0
for palavra in conteudo.split():
    for letra in palavra:
        palavra.swapcase()
        if palavra == "banana":
        	contador +=1
print(contador)