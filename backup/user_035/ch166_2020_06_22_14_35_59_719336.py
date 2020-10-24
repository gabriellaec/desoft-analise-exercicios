def total_do_semestre_por_bairro(dic_gastos):
    soma = 0
    lista_conjunta = dic_gastos.items
    lista_valores = []
    for bairros in dic_gastos:
        i = 0
        while dic_gastos[bairros[i]]<6:
            soma += dic_gastos[bairros[i]]
            i += 1
    return soma
        
            