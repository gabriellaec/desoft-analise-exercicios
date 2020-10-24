def agrupa_por_idade(nomes_idades):
    dicio_faixas = {'criança': [], 'adolescente': [], 'adulto':[],'idoso':[]}
    for nome,idade in nomes_idades.items():
        if idade <= 11:
            faixa = 'criança'
        elif idade <= 17:
            faixa = 'adolescente'
        elif idade <= 59:
            faixa = 'adulto'
        else:
            faixa = 'idoso'
        dicio_faixas[faixa].append(nome)
    return dicio_faixas
