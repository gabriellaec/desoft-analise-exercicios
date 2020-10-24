with open("palavras.txt", "r") as arquivo:
    conteudo = arquivo.read()
contador = 0
lista_de_palavras = conteudo.split()
for word in lista_de_palavras:
    if word.startswith("a") or word.startswith("A"):
        contador += 1
print(contador)