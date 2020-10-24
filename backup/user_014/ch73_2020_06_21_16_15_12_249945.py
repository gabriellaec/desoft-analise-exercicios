def remove_vogais(string):
    string_nova = ''
    for i in range(len(string)):
        if string[i] != 'a' or string[i] != 'e' or string[i] != 'i' or string[i] != 'o' or string[i] != 'u':
            string_nova = string_nova + string[i]
    return string_nova