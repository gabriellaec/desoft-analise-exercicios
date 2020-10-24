lista = [0]*10
i = 1
while lista[-1] != 1:
    lista[i+1] = lista[i]*3 + 1
    lista[i+2] = lista[i+1]/2
    i +=1
print (lista)