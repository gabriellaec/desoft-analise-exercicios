def fatorial(n):
    i=1
    soma=1
    fat=i*(i+1)
   
    while i<=n:
        fat=i
        soma=soma*fat
        i+=1

    return soma


        