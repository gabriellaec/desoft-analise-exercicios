def remove_vogais(palavra):
    i = 0
    lista = list(palavra)
    while i < len(lista):
        if lista[i] == "a" or lista[i] == "e" or lista[i] == "i" or lista[i] == "o" or lista[i] == "u":
            del lista[i]
        
        i += 1
    
    return "".join(lista)