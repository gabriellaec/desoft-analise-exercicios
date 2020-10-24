def agrupa_por_idade(dicionario):
    faixa_etaria = {'criança': [], 'adolescente': [], 'adulto': [], 'idoso': []}
    for nome in dicionario:
        if dicionario [nome] <= 11:
            faixa_etaria["criança"].append(nome)
        elif 17 >= dicionario [nome] >=12:
            faixa_etaria["adolescente"].append(nome)
        elif 59 >= dicionario[nome]>= 18:
            faixa_etaria["adulto"].append(nome)
        else:
            faixa_etaria["idoso"].append(nome) #60 anos ou mais
    return faixa_etaria
                
                