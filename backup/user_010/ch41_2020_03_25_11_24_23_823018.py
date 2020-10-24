lista = [2,-3,4,5,-7,8]
def zera_negativos (x):
    i=0
    while i<len(x):
        if x[i]<0:
            x[i]=0
        i+=1
    return x
resultado = zera_negativos (lista)
print(resultado)