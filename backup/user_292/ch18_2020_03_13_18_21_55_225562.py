def verifica_idade(idade):
    if idade >= 21:
        return 'Liberado_EUA_e_BRASIL'
    elif idade >= 18:
        return 'Liberado_no_BRASIL'
    else:
        return 'Liberado_no_idade'
print(testa_maioridade(17))
print(testa_maioridade(20))
print(testa_maioridade(21))