def agrupa_por_idade(dicionario):
    dicionario2 = {}
    for nome in dicionario:
        crianca = dicionario[nome]
        idoso = dicionario[nome]
        adolescente = dicionario[nome]
        adulto = dicionario[nome]
        for idade in dicionario:
            if idade < 11:
                dicionario2[crianca].append(nome)
            elif idade > 60:
                dicionario2[idoso].append(nome)
            elif idade>12 and idade<17:
                dicionario2[adolescente].append(nome)
            else:
                dicionario2[adulto].append(nome)
        return dicionario2
                
                