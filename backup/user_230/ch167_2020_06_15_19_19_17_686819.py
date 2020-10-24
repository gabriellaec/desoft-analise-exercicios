def bairro_mais_custoso(dicio):
    maior=0
    nome=0
    gasto=0
    novo_dicio={}
    for bairro in dicio:
        novo_dicio[bairro]=sum(dicio[bairro][6:])
    for bairro in novo_dicio:
        if novo_dicio[bairro]>maior:
            maior=novo_dicio[bairro]
            nome=bairro
    return nome
