def total_do_semestre_por_bairro(dic):
    dic_gastos = {}
    for bairro in dic:
        c = 5
        while c < 11:
            for i in dic[bairro]:
                dic_gastos[bairro] += i 
            c +=1 
    return dic_gastos
        
    