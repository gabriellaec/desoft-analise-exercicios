import math
def calcula_pi(n):
    lista=[]
    i = 1
    while i <= n:
        pi =(6/(i**2))
        lista.append(pi)
        i+=1
    return math.sqrt(sum(lista))
print(calcula_pi(10000))