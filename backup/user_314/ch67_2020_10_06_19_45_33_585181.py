def alunos_impares (lista):
    lista_p=[]
    i=0

    while i<(len(lista)-1):

        if(i%2!=0):
            lista_p.append(lista[i])
        i+=1
  
    return lista_p