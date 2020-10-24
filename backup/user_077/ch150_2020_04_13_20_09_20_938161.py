import math
def calcula_pi(n):
    itens=[]*n
    i=0
    for i in range(0,n):
        itens.append(6/((i+1)**2))
        i=i+1
    a=sum(itens)
    b=math.sqrt(a)
    return b
    