def remove_vogais(palavra):
    i=0
    vogais=['a','e','i','o','u']
    while i<len(palavra):
        if palavra[i] in vogais:
            del palavra[i]
        i+=1
    return palavra