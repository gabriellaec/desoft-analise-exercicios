def remove_vogais(a):
    vogais = ['a','e','i','o','u']
    lista = list()
    for i in a:
        for t in vogais:
            if i != t:
                if i not in lista:
                    lista.append(i)
            break