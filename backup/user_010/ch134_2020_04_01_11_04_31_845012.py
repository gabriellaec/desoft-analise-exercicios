
def verifica_quadrado_perfeito (x):
    m=x
    i=0
    lista= [2]
    while m>0:
        lista.append (lista [i] + 2)
        m=m-lista [i]
        i+=1
    if m**2==x:
        return True
    else:
        return False
n=196
resultado=verifica_quadrado_perfeito (n)
print (resultado)