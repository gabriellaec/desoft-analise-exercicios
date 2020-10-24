def remove_vogais(string):
    semvogais = ""
    i=0
    while i<len(string):
        if string[i] not in ["a","e","i","o","u"]:
            semvogais += string[i]
    return semvogais
        
        
    