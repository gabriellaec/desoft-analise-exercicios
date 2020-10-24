def remove_vogais (p):
    lista = ['a','e','i','o','u']
    for element in p:
        if element in lista:
            p.replace(element , '')
            
    return p


