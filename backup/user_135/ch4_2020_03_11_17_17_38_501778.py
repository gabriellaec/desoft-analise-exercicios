def classifica_idade(idade):
    if idade <= 12:
        classificacao = crianca
        return classificacao
    elif idade > 12 and idade < 18:
        classificacao = adolescente
        return classificacao
    else:
        classificacao = adulto
        return classificacao

i = 15
classifica = classifica_idade(i)
print (classifica)