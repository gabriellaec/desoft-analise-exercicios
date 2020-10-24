def junta_nome_sobrenome(x,y):
    z= " "
    i=0 
    lista = []
    while i< len(x):
        f = x[i]+ z +y[i]
        lista.append(f)
        i+=1
    return lista