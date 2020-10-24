def zera_negativos():
lista = [0,-2,8,-5,-23]
i = 0
while i<len(lista):
    if lista[i]<0:
        lista[i] = 0
    i += 1
print(lista)