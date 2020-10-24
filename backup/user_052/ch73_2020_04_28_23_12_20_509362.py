def remove_vogais (string):
    b = "aeiou"
    lista = []
    for i in string:
        if i not in b:
            lista.append(i)
    return "".joint(lista)
        
    