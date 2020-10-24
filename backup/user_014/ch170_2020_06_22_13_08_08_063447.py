def apaga_repetidos (string):
    string_nova = ''
    for i in range (len(string)):
        if string[i] not in string_nova:
            string_nova = string_nova + string[i]
        else:
            string_nova = string_nova + '*'
    return string_nova