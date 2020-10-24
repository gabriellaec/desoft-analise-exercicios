def remove_vogais(string):
    i = 0
    lista = []
    while i < len(string):
        if string[i] == "a" and i == "e" and i == "i" and i == "o" and i == "u":
            lista.append(string[i])
        i +=1
    return ''.join(lista)
            
        