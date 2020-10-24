comando = True
lista = []
while comando:
    pergunta=input("Escolha a palavra: ")
    lista.append(pergunta)
    if pergunta == "fim":
        t=0
        letra = lista[t]
        while t<len(lista):
            if letra[0] != "a":
                del lista[t] 
        comando = False
print(lista)
