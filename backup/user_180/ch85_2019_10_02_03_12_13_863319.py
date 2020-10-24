with open("macacos-me-mordam.txt", "r") as arquivo:
    conteudo = arquivo.read()
contador_banana = 0
for palavra in conteudo.split():
    for letra in palavra:
    	letra.upper()
        if palavra == "banana":
        	contador_banana +=1
print(contador_banana)