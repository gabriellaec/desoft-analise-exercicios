def agrupa_por_idade(dicio):
    dicionario = {}
    lista_c = []
    lista_adol = []
    lista_adul = []
    lista_i = []
    for idade in dicio.values():
        if idade <= 11:
            lista_c.append(dicio[nome])
        elif idade >= 12 and idade <= 17:
            lista_adol.append(dicio[nome])
        elif idade >= 18 and idade <= 59:
            lista_adul.append(dicio[nome])
        elif idade >= 60:
            lista_i.append(dicio[nome])
            
    dicionario['criança'] = lista_c
    dicionario['adolescente'] = lista_adol
    dicionario['adulto'] = lista_adul
    dicionario['idoso'] = lista_i
    return dicionario
     
        