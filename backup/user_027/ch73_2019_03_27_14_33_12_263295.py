def remove_vogais(x):
    vogais = ['a','e','i','o','u']
    for a in x:
        if a in vogais:
            vogais[vogais.find(a)].replace[a,'']
    return x