import math
def calcula_norma(n):
    s=0
    i=0
    while i < len(n):
        s+=(n[i])**2
        print(s)
        i+=1
    norma=math.sqrt(s)
    return norma