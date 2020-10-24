i = 0
lista = [0] * 100

while i < 100:
    lista[i] = 1/(2 ** i)
    i += 1
    
print(sum(lista))
