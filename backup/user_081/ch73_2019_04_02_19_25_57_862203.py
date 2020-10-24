def remove_vogais(string):
    i = 0 
    lista = ['a','e','i','o','u']
    string2 = ''
    while i < len(string):
        if string[i] not in lista:
            string2 += string[i]
            i = i + 1 
        else:
            i = i + 1 
            
    print(string2)