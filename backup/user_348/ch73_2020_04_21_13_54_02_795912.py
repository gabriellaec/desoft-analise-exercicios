def remove_vogais (string):
    i = 0
    while i < len(palavra):
        if string[i] == 'a' or string[i] == 'e'or string[i] == 'i' or string[i] == 'o' or string[i] == 'u':
            del string[i]
        return string
        