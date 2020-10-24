def remove_vogais(p):
    lista_vogais=['a','e','i','o','u']
    for i in range(len(p)):
        if p[i] in lista_vogais:
            del p[i]
    return p
