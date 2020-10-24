def alunos_impares(lista):
    cont=1
    lista_impares=[]
   
    while cont<len(lista):
        if cont%2!=0:
            lista_impares.append(lista[cont])
        cont+=1
    return lista_impares