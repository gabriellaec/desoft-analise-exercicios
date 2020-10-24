def remove_vogais(string):
    nova_string = ''
    i = 0
    while i < len(string):
        if string[i] != 'A' and string[i] != 'E' and string[i] != 'I' and string[i] != 'O' and string[i] != 'U':
            nova_string += string[i]
        i += 1
    return nova_string