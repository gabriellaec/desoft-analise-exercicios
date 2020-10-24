def remove_vogais(string):
    i = 0
    lista = []
    while i < len(string):
        if string[i] == "a" and string[i] == "e" and string[i] == "i" and string[i] == "o" and string[i] == "u":
            lista.append(string[i])
        i +=1
    return ''.join(lista)
            
        