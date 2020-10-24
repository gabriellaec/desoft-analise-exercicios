def apaga_repetidos (string):
    i = 0
    string_nova = ''
    while i < len(string):
        if string[i] not in string_nova:
            string_nova = '' + string[i]
        else:
            string_nova = '' + '*'
        i += 1
    return string_nova