def alunos_impares(nomes):
    
    lista3 = []
       
    i = 0
    
    while i < len(nomes):  
        
        if i % 2 != 0:
    
            lista3.append(nomes[i])
        
        i += 1

    return lista3