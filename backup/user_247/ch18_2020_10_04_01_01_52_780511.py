idade_pessoa= int(input("Qual a sua idade?"))
def verifica_idade(idade_pessoa):
    if idade_pessoa < 18:
        return "Não está liberado"
    elif 18 < idade_pessoa < 21:
        return "Liberado BRASIL"
    else:
        return "Liberado EUA e BRASIL"
    