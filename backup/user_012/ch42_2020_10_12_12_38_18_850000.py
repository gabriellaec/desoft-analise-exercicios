palavra = input('Digite uma palavra: ')
lista1 = []

while palavra != 'fim':
    lista1.append(palavra)
    palavra = input('Digite uma palavra: ')
i=0
while i < len(lista1):
    if lista1[i][0] == 'a':
        print(lista1[i])
    i+=1
print(lista1)