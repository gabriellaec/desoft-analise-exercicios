def remove_vogais(string):
    i = 0
    while i < len(string):
        if string[i] == 'a':
            del string[i]
        elif string[i] == 'e':
            del string[i]
        elif string[i] == 'i':
            del string[i]   
        elif string[i] == 'o':
            del string[i]
        elif string[i] == 'u':
            del string[i]
        else:
        i += 1        
    return string