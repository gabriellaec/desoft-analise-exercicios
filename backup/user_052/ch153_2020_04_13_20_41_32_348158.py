def agrupa_por_idade (D):
    faixa_etaria = {"criança": [],"adolescente": [],"adulto": [],"idoso": []}
    for key in D:
        if D[key] <= 11:
            faixa_etaria["criança"].append(key)
        elif D[key] >= 12 and D[key] <= 17:
            faixa_etaria["adolescente"].append(key)
        elif D[key] >= 18 and D[key] <= 59:
            faixa_etaria["adulto"].append(key)
        else:
            faixa_etaria["idoso"].append(key)
    print(faixa_etaria)
        