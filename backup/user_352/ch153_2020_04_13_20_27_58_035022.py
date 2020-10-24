def agrupa_por_idade(nome_idade):
    faixa_etaria_nome={}
    for nome in nome_idade:
        if nome_idade[nome]<=11:
            faixa_etaria_nome[crinca]=nome
        elif nome_idade[nome]>11 and nome_idade[nome]<=17:
            faixa_etaria_nome[adolecente]=nome
        elif nome_idade[nome]>18 and nome_idade[nome]<=59:
            faixa_etaria_nome[adulto]=nome
        else:
            faixa_etaria_nome[idoso]=nome
            
            
    