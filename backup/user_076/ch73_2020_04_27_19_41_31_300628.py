def remove_vogais(string):
    for i in string:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            semvogais = string.replace(i,"")
    return semvogais

print (remove_vogais('carolina'))
    