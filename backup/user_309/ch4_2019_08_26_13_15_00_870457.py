def classifica_idade(idade):
    if idade <= 11:
        return "crianca"
    elif idade >=12 and idade <= 17:
        return "adolescente"
    else:
        return "adulto" 
idade = int(input("Digite a idade: "))
print(classifica_idade(idade))