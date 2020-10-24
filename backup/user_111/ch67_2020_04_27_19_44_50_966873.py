def alunos_impares(nomes):
    i=0
    lista_impares=[]
    while i<len(nomes):
        if i%2!=0:
            lista_impares.append(nomes[i])
        i+=1
    return lista_impares