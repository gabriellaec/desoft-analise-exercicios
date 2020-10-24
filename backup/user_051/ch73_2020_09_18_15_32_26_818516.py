def remove_vogais(stri):
    lista=['a','e','i','o','u']
    for i in lista:
        stri=stri.replace(i,'')
    return stri