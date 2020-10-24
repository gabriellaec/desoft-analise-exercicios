def agrupa_por_idade(dicionario):
    dicionario2 = {}
    for nome in dicionario:
        idade = dicionario[nome]
        if idade in dicionario2:
            crianca = dicionario2[idade]
            adulto = dicionario2[idade]
            idoso = dicionario2[idade]
            adolescente = diconario2[idade]
            if idade <11:
                dicionario2[crianca].append(nome)
            elif idade>60:
                dicionario2[idoso].append(nome)
            elif idade>12 and idade <17:
                dicionario2[adolescente].append(nome)
            else:
                dicionario2[adulto].append(nome)
                
    return dicionario2