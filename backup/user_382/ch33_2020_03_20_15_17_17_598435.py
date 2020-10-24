import random as r 
def primos_entre(a,b):
    for a > b:
        
        n = r.randint(a,b)
        t = 0 
        num = 2 
        lista = [0]*n
        while n > t:
            div = 2 
            while num >= div:
                if num % div == 0:
                    break 
                else:
                    div += 1
            if num == div:
                lista[t] = num 
                t+=1
            num += 1 
    return lista 