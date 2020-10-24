import math

def seno(x):
    seno=(4*x*(180-x))/(40500-x*(180-x))
    return seno

lista=[]
x=0
while x<=90:
    if seno(x) != math.sin(x):
        lista.append(abs(x))
        x+=1
    else:
        x+=1

lista_ordenada=sorted(lista)

print(lista_ordenada[-1])
    
    