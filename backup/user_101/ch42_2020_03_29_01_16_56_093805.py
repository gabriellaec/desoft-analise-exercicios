sem_fim = True
lista = []
while sem_fim:
    palavra = input("Escreva uma palavra: ")
    if palavra != "fim":
        lista.append(palavra)
    sem_fim = False

for e in lista:
    if e[0] == "a":
    print (e)