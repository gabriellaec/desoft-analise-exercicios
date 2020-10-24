def tamanho_collatz(i):
    tamanho= 1
    while i!= 1:
        if i%2==0:
            i/= 2
        else:
            i= i*3 + 1
        tamanho+= 1
    return tamanho
i=1
maior_tamanho= 0
inicial= 0
while i<1000:
    
    tamanho= tamanho_collatz(i)
    if tamanho > maior_tamanho:
        maior_tamanho= tamanho
        inicial= i
    i+= 1
print (inicial)