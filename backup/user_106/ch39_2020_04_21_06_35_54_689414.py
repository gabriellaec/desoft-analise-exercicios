def tamanho(n):
    contador=1
    while n>1:
        contador+=0
        if n%2==0:
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

lissta=range(1,1000)
print(mais_longo(lissta))