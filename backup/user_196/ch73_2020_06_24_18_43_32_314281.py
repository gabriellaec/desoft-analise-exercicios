def remove_vogais(string):
    stringsemvogal = string
    vogais = ('a', 'e', 'i', 'o', 'u')
    for i in string:
        if i in vogais:
            stringsemvogal = stringsemvogal.replace(i,"")
    return stringsemvogal
