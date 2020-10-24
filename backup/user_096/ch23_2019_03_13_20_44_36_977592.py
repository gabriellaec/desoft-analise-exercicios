
def verifica_idade(idade):
    if idade>21:
        return"Liberado EUA e BRASIL"
    elif 18<idade<21:
        return"Liberado BRASIL"
    elif idade<18:
        return"Não está liberado"
        