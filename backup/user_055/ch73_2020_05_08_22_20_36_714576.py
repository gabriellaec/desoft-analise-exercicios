def remove_vogais(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for c in string:
        if c in vowels:
            string = string.replace(c, '')
    return string