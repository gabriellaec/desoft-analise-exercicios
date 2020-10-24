import math
def calcula_pi(x):
    lista=[]
    i = 1
    while i <= x:
        pi =(6/(i**2))
        lista.append(pi)
        i+=1
    print(sum(lista))