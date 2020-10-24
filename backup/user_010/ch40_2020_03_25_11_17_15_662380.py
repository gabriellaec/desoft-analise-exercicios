lista = [5,6,7,8]
def soma (x):
    s=0
    i=0
    while i<len (x):
        s+=x[i]
        i+=1
    return s
resultado = soma (lista)
print (resultado)