def junta_nome_sobrenome(listaN, listaS):
    listaSN=[]
    i=0
    while i < len(listaN):
        NC=listaN[i]+" "+listaS[i]
        listaSN.append(NC)
        i+=1
    return listaSN
listaN=['s','e','r']
listaS=['z','x','c']
print (junta_nome_sobrenome(listaN, listaS))