#Função que recebe a idade da pessoa e diz se ela está liberada legalmente para comprar álcool no Brasil e/ou nos EUA
def verifica_idade(n):
    if n >= 21:
        return "Liberado EUA e BRASIL"
    elif n >= 18 and n < 21:
        return "Liberado BRASIL"
    else:
        return "Não está liberado"