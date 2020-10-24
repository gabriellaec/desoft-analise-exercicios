def total_do_semestre_por_bairro(dic_gastos):
    soma = 0
    lista_conjunta = dic_gastos.items
    lista_bairros = dic_gastos.values
    lista_valores = []
    for bairros in dic_gastos:
        for i in range(len(bairros)<6):
            soma += i
        x = dict(zip(lista_bairros, soma))
    return x
        
            