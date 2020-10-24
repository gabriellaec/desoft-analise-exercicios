def remove_vogais(string):
    i = 0
    while i < len(string):
        if string[i] == 'a' or 'e' or 'i' or 'o' or 'u':
            del string[i]
    return string
        