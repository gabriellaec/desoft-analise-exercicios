def agrupa_por_idade (dicionario_inicial):
    dicionario_final = {}
    for nome, idade in dicionario_inicial.items():
        if idade <= 11:
            faixa_etaria = 'criança'
        elif iidade>= 12 and idade <= 17:
            faixa_etaria = 'adolescente'
        elif idade>= 18 and idade <= 59:
            faixa_etaria = 'adulto'
        else:
            faixa_etaria = 'idoso'
        dicionario_final[faixa_etaria] = nome
    return dicionario_final