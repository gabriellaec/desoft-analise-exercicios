arquivo = open("palavras.txt", "r")

dicionario_de_palavras = {}

for palavra in arquivo.read().split():
    if palavra not in dicionario_de_palavras:
        dicionario_de_palavras[palavra] = 1
    else:
        dicionario_de_palavras[palavra] += 1
arquivo.close()

lista_de_valores = []

for palavra in dicionario_de_palavras:
    if palavra[0] == "a" or palavra[0] == "A":
        lista_de_valores.append(dicionario_de_palavras[palavra])

print(sum(lista_de_valores))
