def remove_vogais(string):
    for i in string:
        if i in ['a', 'e', 'i', 'o', 'u']:
            palavra = string.replace(i, "")
            return palavra
