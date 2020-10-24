def agrupa_por_idade(nomes):
    kids = []
    teens = []
    adults = []
    idosos = []
    
    for i in nomes:
        if nomes[i] <= 11:
            kids.append(i)
        if 11 < nomes[i] <= 17:
            teens.append(i)
        if 17 < nomes[i] <= 59:
            adults.append(i)
        if nomes > 59:
            idosos.append(i)
    faixas = {"criança" : kids, "adolescente" : teens, "adulto" : adults, "idoso" : idosos}
    return faixas