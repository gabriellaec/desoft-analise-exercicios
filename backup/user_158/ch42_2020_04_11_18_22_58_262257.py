palavra = input(' escreva uma palavra')
lista =[]
i=0
while palavra != 'fim':
    lista.append(palavra)
while i < len(lista):
    palavra =lista[i]
    if len(palavra)>0 and palavra[0] == 'a':
        print(palavra)
    i += 1