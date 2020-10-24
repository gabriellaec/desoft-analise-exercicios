def classifica_idade (idade):
    if idade <= 11:
        resultado = 'crianca'
        return resultado
    elif idade <= 12 and idade < 18:
        resultado = 'adolescente'
        return resultado
    else:
        resultado = 'adulto'
        return resultado

i = 23
    
funcao = classifica_idade (i)
print (funcao)