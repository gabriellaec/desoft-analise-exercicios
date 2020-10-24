def agrupa_por_idade(dicio):
    cri = []
    ado = []
    adu = []
    ido = []
    idade = {}
    for k, v in dicio.items():
        if v <= 11:
            cri.append(k)
        elif v >= 12 and v <= 17:
            ado.append(k)
        elif v >= 18 and v <= 59:
            adu.append(k)
        else:
            ido.append(k)
    idade['criança'] = cri
    idade['adolescente'] = ado
    idade['adulto'] = adu
    idade['idoso'] = ido
    return idade