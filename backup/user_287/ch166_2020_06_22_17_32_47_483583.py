def total_do_semestre_por_bairro(dicionario):
    
    dic2= dict()
    
    for k in dicionario:
        
        for i in range(6,12):
            
            if not k in dic2:
                dic2[k] = dicionario[k][i]
            else:
                dic2[k] += dicionario[k][i]

    return dicionario2
        