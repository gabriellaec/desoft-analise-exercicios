def total_do_semestre_por_bairro(dic):
    soma = 0 
    for bairro in dic:
        c = 5
        while c < 12:
            soma += bairro[c]
            c +=1 
    return soma 
        
        
    