def remove_vogais(string):
    i = 0
    while i < len(string):
        string_nova = []
        if string[i] != 'a' or string[i] != 'e' or string[i] != 'i' or string[i] != 'o' or string[i] != 'u':
            string_nova.append(string)
        i += 1
    return string_nova