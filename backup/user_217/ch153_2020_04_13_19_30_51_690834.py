def funcRecebeDic(dic):
    faixa_etaria = {'criança': [], 'adolescente': [], 'adulto': [], 'idoso': []}
    for k, v in dic.items():
        if v <= 11:
            faixa_etaria['criança'].append(k)
        elif v <= 17:
            faixa_etaria['adolescente'].append(k)
        elif v <= 59:
            faixa_etaria['adulto'].append(k)
        else:
            faixa_etaria['idoso'].append(k)
    return faixa_etaria