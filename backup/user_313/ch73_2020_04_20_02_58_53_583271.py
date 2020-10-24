def remove_vogais(a):
    vogais = ['a','e','i','o','u']
    lista = list()
    for i in a:
        lista.append(i)      
        for t in vogais:
            if i == t:
                lista.remove(i) 
    return("".join(lista))