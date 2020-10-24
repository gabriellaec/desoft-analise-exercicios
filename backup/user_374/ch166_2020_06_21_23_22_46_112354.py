
def total_do_semestre_por_bairro(dicionario):
    dicionario_retorno = {}
    for bairro in dicionario:
        dicionario_retorno[bairro] = sum(dicionario[bairro][6:])
    return dicionario_retorno
