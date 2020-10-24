with open(macacos-me-mordam.txt, "r") as arquivo:
    conteudo = arquivo.read()
contador_banana = 0
for palavra in conteudo.split():
    if palavra == "banana".upper():
        contador +=1
print(contador)
        