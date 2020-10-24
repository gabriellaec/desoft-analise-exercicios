pergunta = input("digite palavras: ")
lista = []
while pergunta != "fim":
    lista.append(pergunta)
    pergunta = input("digite palavras: ")
    
for e in lista:
    if e[0] == "a":
        print(e)
        