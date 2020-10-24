def remove_vogais(string):
    x = string
    i = 0
    while i < len(string):
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            x -= i
        i += 1
        
    return x