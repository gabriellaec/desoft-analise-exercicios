def total_do_semestre_por_bairro(dicio_gastos):
    gasto_total = {}
    i = 0
    numero = 0
    for bairro, lista in dicio_gastos.items():
        while i < len(lista):
            numero += lista[i]
        gasto_total[bairro] = numero
    return gasto_total
        
        
    
    