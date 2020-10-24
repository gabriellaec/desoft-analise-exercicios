def remove_vogais(string):
    for i in string:
        if i =='a':
            semvogais = string.replace(i,"")
        if i=='e':
            semvogais = string.replace(i,"")
        if i=='i':
            semvogais = string.replace(i,"")
        if i=='o':
            semvogais = string.replace(i,"")
        if i=='u':
            semvogais = string.replace(i,"")
    return semvogais

print (remove_vogais('carolina'))
    