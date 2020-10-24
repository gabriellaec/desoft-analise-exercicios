def remove_vogais(s):
    i = 0
    lista = []
    while i < len(s):
        if s[i] == "a" and s[i] == "e" and s[i] == "i" and s[i] == "o" and s[i] == "u":
            lista.append(s[i])
        i +=1
    return ''.join(lista)
            
        