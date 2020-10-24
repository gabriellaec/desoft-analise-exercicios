def teste_maioridade(idade):
    if idade >= 21:
        return 'liberado EUA e BRASIL'
    elif idade >= 18:
        return 'liberado BRASIL'
    else:
        return 'Não está liberado'
a = int(input('Qual sua idade?'))
 
