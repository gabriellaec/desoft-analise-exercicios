def esconde_senha(string):
    string2 = []
    for 'letra' in string:
        string2.append(string.replace('letra', '*'))
    return string2