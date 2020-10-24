def agrupa_por_idade(dici1):
    saida={'criança':[],'adolescente':[],'adulto':[],'idoso':[]}
    for nome,idade in dici1.items():
        if idade <= 11:
            saida['criança'].append(nome)
        elif idade <= 17:
            saida['adolescente'].append(nome)
        elif idade <=59:
            saida['adulto'].append(nome)
        else:
            saida['idoso'].append(nome)
    return saida
            