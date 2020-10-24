lista1 = [1,2,3,4,5,6]
lista2 = [4,5,6,7,8,9]

t = 0
while t<len(lista1):
    if lista1[t] in lista2:
        del lista1[t]
        t+=1
    else:
        t+=1

print(lista1)