def remove_vogais(palavra):
    i = 0
    lista = list(palavra)
    x = []
    while i < len(palavra):
        if lista[i] == "a" or lista[i] == "e" or lista[i] == "i" or lista[i] == "o" or lista[i] == "u":
            i += 1
        
        else:
            x.append(lista[i])
            i += 1
    
    return "".join(x)