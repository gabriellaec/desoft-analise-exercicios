def remove_vogais (string):
    i = 0 
    soma="t" 
    while i < len(string):
        if string[i] != "a" or string [i] != "e" or string [i] != "i" or string [i] != "o" or string [i] != "u":
            soma = soma + string [i]
            i += 1 
        i += 1
    return soma   
            
                                