def numero_no_indice(lista):
    resp=[]
    for a in range(len(lista)):
        print(a)
        if a==lista[a]:
        	resp.append(lista[a])
    return resp
lista=[2,3,2,1]
print(numero_no_indice(lista))

