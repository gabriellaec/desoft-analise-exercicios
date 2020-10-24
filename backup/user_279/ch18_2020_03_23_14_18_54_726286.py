def verifica_idade(idade):
    
    idade = int(input("qual a sua idade:"))
    if idade >= 21:
        return("Liberado EUA e Brasil")
    elif 21 > idade >= 18:
        return("Liberado Brasil")
    elif idade < 18:
        return("Não está liberado")