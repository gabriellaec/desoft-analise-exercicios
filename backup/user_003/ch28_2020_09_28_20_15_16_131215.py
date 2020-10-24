lista = [0]*100
soma=0
i = 0
elevado = 0
while elevado < 100:
    x = 2 ** elevado
    lista[i] = 1 / x
    elevado += 1
    i =i  +1
a=0
for e in lista:
    soma = lista[a] + lista[a+1]

print(soma)
