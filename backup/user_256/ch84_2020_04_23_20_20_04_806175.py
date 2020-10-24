def inverte_dicionario(pessoa_pra_idade):
    idade_pra_pessoa = {}
    for pessoa, idade in pessoa_pra_idade.items():
        if not idade in idade_pra_pessoa:
            idade_pra_pessoa[idade] = [pessoa]
        else:
             idade_pra_pessoa[idade] =  idade_pra_pessoa[idade] + pessoa
    print (idade_pra_pessoa)    
    return idade_pra_pessoa
        