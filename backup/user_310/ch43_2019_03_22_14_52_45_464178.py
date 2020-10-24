umero= 1000


def tamanho_sequencia(n):
    atual=n
    tamanho=0
    while atual>1:
        if atual%2==0:
            tamanho+=1
            atual=atual/2
        
        else:
            tamanho+=1
            atual=3*atual+1
        
    return tamanho+1


maior_sequencia=0

i=numero

while i>0:
    if tamanho_sequencia(i)> maior_sequencia:
        maior_sequencia=i
    i-=1