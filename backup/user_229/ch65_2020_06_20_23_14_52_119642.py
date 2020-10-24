def capitaliza(string):
    nova_palavra = string
    maiuscula = string.upper()
    letra_maiuscula = nova_palavra.replace('{}'.format(string[0]), '{}'.format(maiuscula[0]))
    letra_minuscula = nova_palavra[1:]
    apenas_letra_maiuscula = letra_maiuscula[0]
    apenas_letra_maiuscula += letra_minuscula

    return apenas_letra_maiuscula