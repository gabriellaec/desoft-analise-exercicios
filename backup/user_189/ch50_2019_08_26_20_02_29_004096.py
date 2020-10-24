def numero_no_indice(lista):
    resp=[]
    for a in len(lista):
        if a==lista[a]:
        	resp.append(lista[a])
    return resp
lista=[0,1,3,2,4]
print(numero_no_indice(lista))

