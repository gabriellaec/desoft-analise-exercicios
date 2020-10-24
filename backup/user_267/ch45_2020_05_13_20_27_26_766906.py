digite = int(input('Dite um inteiro positivo: '))
lista = []
new = []
while digite > 0:
    lista.append(digite)
    digite = int(input('Dite um inteiro positivo: '))
for n in range(len(lista)-1,0,-1):
    new.append(lista[n])
print(new)
    
    