from math import sin,degrees,radians

#Criando listas
graus = list()
lista = list()

#Criando lista dos valores em graus para analisar a diferença. 
i = 0
while i<91 :
    graus.append(i)
    i+=1

#Percorrendo a lista em graus 
for x in graus:
    seno_x = (4*x*(180-x))/(40500 - x*(180-x))
    
    mat = sin((radians(x)))

    diferenca = abs(seno_x - mat)

    lista.append(diferenca)

print(graus[lista.index(max(lista))])