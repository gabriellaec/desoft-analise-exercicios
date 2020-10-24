idade = int(input("Digite a idade da criança: "))
def classifica_idade (x):
    if x <=11:
        resultado = "crianca"
        return resultado
    elif x >= 18:
        resultado = "adulto"
        return resultado
    else:
        resultado = "adolescente"
        return resultado
funcao = classifica_idade (idade)
print (idade)
print (funcao)