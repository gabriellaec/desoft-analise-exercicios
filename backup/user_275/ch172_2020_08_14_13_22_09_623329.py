def verifica_idade(idade):
    if idade < 18:
        return 'jovem'
    elif idade < 60:
        return 'adulto'
    else:
        return 'idoso'