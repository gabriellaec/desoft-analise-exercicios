def classifica_idade(idade):
    if idade <= 11:
        classificacao = crianca
        return classificacao
    elif idade > 11 and idade < 18:
        classificacao = adolescente
        return classificacao
    else:
        classificacao = adulto
        return classificacao