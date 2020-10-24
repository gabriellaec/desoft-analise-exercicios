# FUNÇÃO DO EXERCÍCIO 166
def total_do_semestre_por_bairro(gastos_12_meses):
    
    resultado = dict(gastos_12_meses)
    
    for bairro in gastos_12_meses.keys():
        resultado[bairro] = sum(gastos_12_meses[bairro][6:])
    
    return resultado


def bairro_mais_custoso(gastos_12_meses):
    
    gastos_totais_semestre = total_do_semestre_por_bairro(gastos_12_meses)
    invertido = dict()
    
    for bairro in gastos_totais_semestre.keys():
        invertido[gastos_totais_semestre[bairro]] = bairro
    
    return invertido[max(gastos_totais_semestre.values())]

