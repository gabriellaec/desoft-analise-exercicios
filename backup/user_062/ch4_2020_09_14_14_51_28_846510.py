def classifica_idade(idade):
    if idade <= 11:
        print ('Você é uma criança')
    elif idade >12 and idade <17:
        print ('Você já é adolescente')
    elif idade >= 18:
        print ('Você é adulto')
    return classifica_idade

idade = float(input('Quantos anos você tem?'))
print(classifica_idade(idade))