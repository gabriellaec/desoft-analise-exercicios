def calcula_media (lista):
    lista_notas= []
    for dic in lista:
        for aluno in dic:
            nota = dic[aluno]
            lista_notas.append(nota)
    i=0
    soma = 0
    while i<len(lista_notas):
        soma += lista_notas[i]
        i+=1
    
    média = soma/len(lista_notas)
    
    return média
        
        