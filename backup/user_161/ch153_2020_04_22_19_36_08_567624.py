def agrupa_por_idade(dic):
    faixa_etaria = {'criança': [], 'adolescente': [], 'adulto': [], 'idoso': []}
    for nome in dic:
        if dic[nome] <= 11:
            faixa_etaria["criança"].append(nome)
        elif 12 <= dic[nome] <= 17:
            faixa_etaria["adolescente"].append(nome)
        elif 18 <= dic[nome] <= 59:
            faixa_etaria["adulto"].append(nome)
        else: #60 anos ou mais
            faixa_etaria["idoso"].append(nome)
    return faixa_etaria