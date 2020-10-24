lista = []
while True:
    l = int(input('Números:'))
    if l > 0:
        lista.append(l)
    else:
        break

lista_i = []
i = 1
while i <= (len(lista)):
    lista_i.append(lista[len(lista)-i])
    i += 1
        
    
print(lista_i)