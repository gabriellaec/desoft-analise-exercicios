a = 1
lista = []
while a!=0:
    pergunta = input("Digite palavras ae mano: ")
    lista.append(pergunta)
    if pergunta == "fim":
        a = 0
for i in range(len(lista)):
    pergunta = lista[i]
    if pergunta[0]=="a":
        print (pergunta)
            
    