with open("macacos-me-mordam.txt", 'r') as arquivo:
    conteudo = arquivo.read()

contador_b = 0
conteudo = conteudo.split()
for string in conteudo:
    palavra = string.lower()
    if palavra == "banana":
        contador_b +=1
print(contador_b)
    