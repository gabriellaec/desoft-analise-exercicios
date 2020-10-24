def calcula_valor_devido (valor, meses, taxa):
    if meses == 0:
        return 'O número de meses não pode ser zero.'
    elif valor == 0:
        return 'O valor não pode ser zero.'
    elif taxa == 0:
        return 'A taxa não pode ser igual a zero.'
    else:
        valor_devido = (valor * ((1 + taxa) ** meses))
        return valor_devido

valor_teste = 1000
meses_teste = 2
taxa_teste = 3/10

teste_funcao = calcula_valor_devido(valor_teste, meses_teste, taxa_teste)

if teste_funcao == (valor_teste * ((1 + taxa_teste) ** meses_teste)):
    print('Validado')
else:
    print('Erro!')

print(teste_funcao)