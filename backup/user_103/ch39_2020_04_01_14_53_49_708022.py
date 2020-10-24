def collatz(primeiro_termo):
    novo_termo=0
    if primeiro_termo<1000:
        if primeiro_termo%2==0:
            novo_termo=primeiro_termo/2
        else:
            novo_termo=(primeiro_termo*3)+1
    n=2
    lista=[0]*n
    lista[0]=primeiro_termo
    lista[1]=novo_termo
    while novo_termo>1:
        if novo_termo52==0:
            novo_termo=novo_termo/2
        else:
            novo_termo=(novo_termo*3)+1
        n+=1
        lista.append(novo_termo)
    return len(lista)

tamanho=0
primeiro=0
i=1
while i<1000:
    m=collatz(i)
    if m> tamanho:
        tamanho=m
        primeiro=1
    i+=1
print (primeiro)
    
    