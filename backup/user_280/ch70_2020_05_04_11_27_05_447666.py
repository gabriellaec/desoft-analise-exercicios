def esconde_senha(string):
    lista = []
    for 'letra' in string:
        lista.append(string.replace('letra', '*'))
    return sum(lista)