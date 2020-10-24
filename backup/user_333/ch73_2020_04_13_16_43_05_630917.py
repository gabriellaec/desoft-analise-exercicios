def remove_vogais(palavra):
    lista_vogais=['a','e','i','o','u']
    for i in range(len(palavra)):
        if palavra[i] in lista_vogais:
            del(palavra[i])
    return palavra