def faixa_etaria(pessoa):
    if pessoa<=11:
        return 'criança'
    elif 12<pessoa<17:
        return 'adolescente'
    elif 18<pessoa<59:
        return 'adulto'
    else:
        return 'idoso'  
def agrupa_por_idade(nome_idade):
    faixa_nomes = {'criança': [], 'adolescente': [], 'adulto': [], 'idoso': []}
    for i in nome_idade:
        if i not in faixa_nomes:
            faixa_nomes[faixa_etaria(nome_idade[i])].append(i)
    print(faixa_nomes)
            