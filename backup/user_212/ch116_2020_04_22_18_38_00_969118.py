def raiz_quadrada(n):
    i=1
    subtracoes=0
    while i<=n:
        n-=i
        i+=2
        subtracoes+=1
    return subtracoes