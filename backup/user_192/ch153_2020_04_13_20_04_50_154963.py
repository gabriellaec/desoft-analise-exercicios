def agrupa_por_idade(nome_idade):
    faixa_nome = dict()
    for nome, idade in nome_idade.items():
        for faixa, nome2 in faixa_nome.items():
            if idade <= 11:
                n_criança = list()
                n_criança.append(nome)
                faixa == criança
                faixa_nome[faixa] = n_criança
            
            if idade <= 17 and idade >= 12:
                n_adol = list()
                n_adol.append(nome)
                faixa == adolescente
                faixa_nome[faixa] = n_adol
            
            if idade <= 59 and idade >= 18:
                n_adulto = list()
                n_adulto.append(nome)
                faixa == adulto
                faixa_nome[faixa] = n_adulto
            
            if  idade >= 60:
                n_idoso = list()
                n_idoso.append(nome)
                faixa == idoso
                faixa_nome[faixa] = n_adulto
    return faixa_nome         
         