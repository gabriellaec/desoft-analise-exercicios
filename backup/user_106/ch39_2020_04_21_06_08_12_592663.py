def tamanho(n):
    contador=0
    while True:
        contador+=1
        if n==1:
            break
        elif n%2==0:
            n=n/2
        else:
            n=3*n+1
    return contador
    
def mais_longo(lista):
    maior=0
    for i in lista:
        if tamanho(i)>maior:
            maior=tamanho(i)
            resposta=i
    return resposta