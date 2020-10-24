def agrupa_por_idade(nome_para_idade):
    faixa_para_nomes = {'criança': [], 'adolescente': [], 'adulto': [], 'idoso': []}
    for nome, idade in nome_para_idade.items():
         if v <= 11:
            faixa = 'criança'
        elif v <=17:
            faixa = 'adolescente'
        elif v <= 59:
            faixa = 'adulto'
        else:
            faixa = 'idoso'
        faixa_para_nomes[faixa].append(nomes)
    return faixa_para_nomes
