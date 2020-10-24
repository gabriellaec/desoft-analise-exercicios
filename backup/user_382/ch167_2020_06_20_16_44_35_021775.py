def total_do_semestre_por_bairro(dic):
    dic2 = {}
    for i in dic:
        total = sum(dic[i][6:])
        dic2[i] = total 
        
    return dic2

def bairro_mais_custoso(dic):
    gasto = total_do_semestre_por_bairro(dic)
    maximo = 0
    for k,v in gasto.items():
        if v > maximo:
            maximo = v 
            bairro = k 
    return bairro 