lista = [0]*100
a=0
elevado = 0
for e in lista:
    lista[a] = 1/ 2 ** elevado
    elevado +=1
    a=a +1
a=0
x=0
soma=0
while x<100:
    soma = soma + lista[a]
    a+=1
    x=x+1
print(soma) 