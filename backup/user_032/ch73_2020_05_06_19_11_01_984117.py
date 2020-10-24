def remove_vogais(strings):
    strings = strings.replace('a','')
    strings = strings.replace('e','')
    strings = strings.replace('i','')
    strings = strings.replace('o','')
    strings = strings.replace('u','')
    return strings
print(remove_vogais(strings)) 