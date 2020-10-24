def remove_vogais(palavra):
    i = 0
    while i in range(0, len(palavra)):
        if palavra[i] == 'a' or 'e' or 'i' or 'o' or 'u':
            palavra = palavra.replace(palavra[i], '')            
            i += 1
        else:
            i += 1
    print (palavra)