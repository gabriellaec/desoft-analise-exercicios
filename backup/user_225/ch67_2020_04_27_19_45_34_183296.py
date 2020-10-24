def alunos_impares(lista):
    i = 0
    listanova = []
    while i < len(lista):
        if i%2!=0:
            listanova.append(lista[i])
        i+=1
    return listanova        