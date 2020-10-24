iguais=[]
lista=[]
def numero_no_indice(lista):
    i=0
    while i<len(lista):
        if i==lista[i]:
            iguais.append(lista[i])
    return iguais
print(numero_no_indice)