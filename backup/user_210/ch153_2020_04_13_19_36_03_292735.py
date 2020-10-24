def agrupa_por_idade(dic):
    faixas_etarias = {"criança": [], "adolescente": [], "adulto": [], "idoso": []}
    for each in dic:
        if dic[each] <= 11:
            faixas_etarias["criança"].append(each)
        elif 11 < dic[each] <= 17:
            faixas_etarias["adolescente"].append(each)
        elif 17 < dic[each] <= 59:
            faixas_etarias["adulto"].append(each)
        else:
            faixas_etarias["idoso"].append(each)
    return faixas_etarias