import math 

graus = list()
lista = []

i = 0
while i<91 :
    graus.append(i)
    i+=1

for x in range(len(graus)):
    seno_x = (4*x*(180-x))/(40500 - x*(180-x))

    mat = math.sin(x)

    diferenca = abs(seno_x - mat)

    lista.append(diferenca)

print(graus[lista.index(max(lista))])