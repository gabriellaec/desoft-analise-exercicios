numeros = [0, 10, 2, 30, 4]
def numero_no_indice (lista):
    real=[]
    for e,i in enumerate(lista):
        if e==i:
            real.append (e)
    return real

print (numero_no_indice(numeros))