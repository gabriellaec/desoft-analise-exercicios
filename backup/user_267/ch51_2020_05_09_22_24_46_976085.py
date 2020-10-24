def eh_primo(n):
    if (n == 0) or (n == 1):
        return False
    elif n == 2:
        return True
    else:
        i = n-2
        if n % 2 == 0:
            return False
        while i>1:
            if n % i == 0:
                return False
            i -= 2
            if i == 0:
                return True
        return True
def primos_entre(a, b):
    r = []
    for n in range(a, b+1):
        if eh_primo(n) == True:
            r.append(n)
    for i in range(0,len(r)-1):        
        c = []        
        for x in r:
            if x[i] < x[i+1]:
                c.append(x)        
        return c
    e = 0
    
#    crescente = []
#    while e <= len(r):
#        if r[e] < r[e+1]:
#            crescente.append(r[e])
#            del(r[e]) #ir deletando os elementos de r pra, ao final, incluir na crescente o último elemento
#            e += 1
#        elif r[e] > r[e+1]:
#            e += 1
#        else:
#            crescente.append(x[e]) 
#    return crescente