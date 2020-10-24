lista = [1]*100
s = lista[0]
for i in range(0,99):
    lista[i + 1] = lista[i]*(1/2)
    s += lista[i+1]
print(s)
