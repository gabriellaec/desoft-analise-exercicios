import math
lista_erros=[]
x=0
while x<90:
    seno_c=(4*x*(180-x))/(40500 - x*(180-x))
    seno_f=math.sin(math.radians(x))
    erro=seno_f-seno_c
    lista_erros.append(abs(erro))
    x+=1

erro_m=max(lista_erros)
#print(erro_m)
print(lista_erros.index(erro_m))
#print(len(lista_erros))
    
