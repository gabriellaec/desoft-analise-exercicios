def remove_vogais (palavra):
    vogais = ['a','e','i','o','u']    
    i = 0
    x = list(palavra)
    while i < len(x):
        if palavra[i] in vogais:
            del palavra[i]
        i+=1
    return palavra
    