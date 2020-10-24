def soma_valores(lista):
    valores = len(lista)
    i = 0
    while i < valores:
        tot += lista[i]
        i += 1
        
listo = [5,5,5,5,5]
print(soma_valores(listo))