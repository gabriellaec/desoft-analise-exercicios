def inverte_dicionario(pessoa_pra_idade):
    idade_pra_pessoa = {}
    for pessoa, idade in pessoa_pra_idade.items():
        idade_pra_pessoa[idade] = pessoa
    return idade_pra_pessoa
        