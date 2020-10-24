perg_p = input("digite uma palavra: ")
lista = []

while perg_p != 'fim':
    lista.append(perg_p)
    perg_p = input("digite outra palavra: ")
    
i = 0
while i < len(lista):
    if lista[i][0] == 'a':
        print(lista[i])
    i += 1