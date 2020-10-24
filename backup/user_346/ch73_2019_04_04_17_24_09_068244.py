def remove_vogais(string):
    i=0
    while i<len(string):
        if string[i]=="a","e","i","o","u":
            del(string[i])
    return string