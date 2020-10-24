def apaga_repetidos(string):
    nova_string = '' 
    for i in range(len(string)):
        if not string[i] in nova_string:
            nova_string += string[i]
        else:
            nova_string += '*'
    return nova_string