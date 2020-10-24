num = 49

def raiz_quadrada (x):

    lista_impares = []
    lista_impares.append (1)
    i=0
    
    sub = []
    sub.append (x-1)
    
    while sub [i]!=0:
        lista_impares.append(lista_impares [i] + 2)
        sub.append (sub [i] - lista_impares [i+1])
        i+=1
    return len (sub)
resultado = raiz_quadrada (num)
print (resultado)
