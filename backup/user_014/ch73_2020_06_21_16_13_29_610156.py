def remove_vogais(string):
    i = 0
    string_nova = ''
    while i < len(string):
        if string[i] != 'a' or string[i] != 'e' or string[i] != 'i' or string[i] != 'o' or string[i] != 'u':
            string_nova = string_nova + string[i]
        i += 1
    return string_nova