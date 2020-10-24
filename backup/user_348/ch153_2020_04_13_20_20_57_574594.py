def agrupa_por_idade (dicionario_inicial):
    dicionario_final = {}
    for nome, i in dicionario_inicial.items():
        if i <= 11:
            faixa_etaria = 'criança'
        elif i>= 12 and i <= 17:
            faixa_etaria = 'adolescente'
        elif i>= 18 and i <= 59:
            faixa_etaria = 'adulto'
        else:
            faixa_etaria = 'idoso'
        dicionario_final['faixa_etaria'] = nome
    return dicionario_final