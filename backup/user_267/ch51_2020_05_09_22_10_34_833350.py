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
    e = 0
    crescente = []
    while e <= len(r):
        if x[e] < x[e+1]:
            crescente.append(x[e])
            del(x[e]) #ir deletando os elementos de r pra, ao final, incluir na crescente o último elemento
            e += 1
        elif x[e] > x[e+1]:
            e += 1
        else:
            crescente.append(x[e]) 
    return crescente