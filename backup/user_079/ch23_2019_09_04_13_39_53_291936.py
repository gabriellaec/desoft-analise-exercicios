def teste_de_maioridade (idade) :
    if idade >= 21:
        return 'USA and BR cleared'
    elif idade >= 18:
        return 'BR cleared'
    else:
        return 'ACCESS DENIED NOT CLEARED'
idade= int(input ('AGE: '))
resultado = teste_de_maioridade(idade)
print(resultado)