def fatorial(n):
    i=0
    diminuir= 1
    outra= n
    multiplicador= 1
    while i<n-1:
        outra-= diminuir
        #print (outra)
        multiplicador*= outra
        i+= 1
    resultado= multiplicador * n
    return resultado