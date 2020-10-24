def lista_palavras(texto):
    with open(texto, 'r') as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()
        return palavras

lista = lista_palavras("macacos-me-mordam.txt")
lista2 = []
i = 0
while i < len(lista):
    if lista[i].upper() == "BANANA":
        lista2.append(lista[i])
    i+=1

print(len(lista2))