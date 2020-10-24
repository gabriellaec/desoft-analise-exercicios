def total_do_semestre_por_bairro(dados):
    resultado = {}
    for i in dados:
        dados[i] = resultado.keys()
        valores = dados.values()
        for valor in valores:
            resultado[dados[i]] = valores[valor]
    return resultado