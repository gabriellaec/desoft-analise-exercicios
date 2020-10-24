
def total_do_semestre_por_bairro(gastos_12_meses):
    
    resultado = dict(gastos_12_meses)
    
    for bairro in gastos_12_meses.keys():
        resultado[bairro] = sum(gastos_12_meses[bairro][6:])
    
    return resultado


