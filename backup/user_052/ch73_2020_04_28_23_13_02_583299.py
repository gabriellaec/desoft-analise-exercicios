def remove_vogais (string):
    b = ["a","e","i","o","u"]
    lista = []
    for i in string:
        if i not in b:
            lista.append(i)
    return "".join(lista)
        
    