def classifica_idade(idade):
    if idade <= 7:
        return "crianca"
    else:
        if idade >= 12 and idade <=17:
            return "adolescente"
        else:
            return "adulto"

idade = int(input("Quantos anos voce tem? "))

print(classifica_idade(idade))
