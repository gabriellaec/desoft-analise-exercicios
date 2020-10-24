def remove_vogais(palavra):
    i=0
    vogais=['a', 'e', 'i', 'o', 'u']
    while i < len(palavra):
        if palavra[i] in vogais:
            palavra=palavra[ :i]+palavra[i+1:]
        i+=1
    return palavra
print(remove_vogais('abobora'))
