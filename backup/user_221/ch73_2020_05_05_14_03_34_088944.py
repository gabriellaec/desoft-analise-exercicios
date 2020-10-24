def remove_vogais(string):
    nova_string = ''
    i = 0
    while i < len(string):
        if string[i] != 'a' and string[i] != 'e' and string[i] != 'i' and string[i] != 'o' and string[i] != 'u':
            nova_string += string[i]
        i += 1
    return nova_string