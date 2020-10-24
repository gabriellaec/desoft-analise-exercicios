lista = []
int(input('Diga o número: '))
i = 0
while lista[i] != 0:
    lista.append(lista[i])
    int(input('Diga o número: '))
    i = i + 1    
print(sum(lista))