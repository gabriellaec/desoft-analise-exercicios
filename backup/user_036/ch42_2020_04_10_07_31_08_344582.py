lista = []
palavra = input('Digite uma palavra: ')
while palavra != 'fim':
    lista.append(palavra)
    palavra = input('Digite outra palavra: ')

#print (lista)
i = 0
for i in lista:
    palavra = lista[i]
    if len(lista) > 1 and palavra[0] == 'a':
        print(palavra)
    i += 1