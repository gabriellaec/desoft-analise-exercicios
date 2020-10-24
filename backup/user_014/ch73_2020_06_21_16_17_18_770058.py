def remove_vogais(string):
    string_nova = ''
    for i in range(len(string)):
        if string[i] != 'a' and string[i] != 'e' and string[i] != 'i' and string[i] != 'o' and string[i] != 'u':
            string_nova = string_nova + string[i]
    return string_nova