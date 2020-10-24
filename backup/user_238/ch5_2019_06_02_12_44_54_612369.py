def primo(p):
    if p >1:
        for x in range (2,p):
            if p%x == 0:
                return False
    else:
        return False
    return True


def maior_primo_menor_que(n):
    lista=[]
    for i in range (n+1):
        primos=primo(i)
        if primos== True:
            lista.append(i)
    
    if len(lista)==0:
        return -1
    maximo=max(lista)
    return maximo

print(maior_primo(6))
    
        