def agrupa_por_idade(dic_nomeidade):
    dic_faixaetaria={}
    for n in dic_nomeidade.keys():
        if dic_nomeidade[n]<=11:
            dic_faixaetaria['crianca']+=n
        elif 12<=dic_nomeidade[n]<=17:
            dic_faixaetaria['adolescente']+=n
        elif 18<=dic_nomeidade[n]<=59:
            dic_faixaetaria['adulto']+=n
        else:
            dic_faixaetaria['idoso']+=n
    return dic_faixaetaria