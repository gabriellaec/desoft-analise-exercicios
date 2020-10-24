def remove_vogais(string):
    i = 0
    while i < len(string):
        if string[i] in string:
            del string[i]
        i +=1
    return string