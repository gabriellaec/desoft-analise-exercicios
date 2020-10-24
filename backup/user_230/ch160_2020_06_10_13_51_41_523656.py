import math

def seno(x):
    seno=(4*x*(180-x))/(40500-x*(180-x))
    return seno

lista_x=[]
lista_resultado=[]
x=0
while (x<=90):
    if abs(seno(x)) != abs(math.sin(math.radians(x))):
        diferenca=abs(abs(seno(x)) - abs(math.sin(x)))
        lista_resultado.append(diferenca)
        lista_x.append(x)
        x+=1
    else:
        x+=1
i=0
maior=0
pos=0
while i<len(lista_resultado):
    if lista_resultado[i]>maior:
        maior=lista_resultado[i]
        pos=i
    i+=1
print(lista_x[pos])