def remove_vogais(palavra):
    i = 0
    consoada = ''
    while i<len(palavra):
        
        if palavra[i] != "a":
            consoada += palavra[i]
            if palavra[i] != "e":
                consoada += palavra[i]
                if palavra[i] != "i":
                    consoada += palavra[i]
                    if palavra[i] != "o":
                        consoada += palavra[i]
                        if palavra[i] != "u":
                            consoada += palavra[i]
    i+=1
    return consoada