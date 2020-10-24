import math
def calcula_pi(n):
    if n==1:
        produto=math.sqrt(6)
    elif n==2:
        produto=math.sqrt(6/4+6)
    else:
        produto=1
        termos=range(1,n+1)
        for o in termos:
            produto= math.sqrt(6/(n**2))+produto
    return produto
