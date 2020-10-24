def remove_vogais(string):
    vogais = ['a', 'e', 'i', 'o', 'u']
    for i in string:
        if i in vogais:
            string = string.replace(i,"")
            
    return string