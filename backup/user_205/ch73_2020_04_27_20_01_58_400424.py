def remove_vogais(palavra):
    x = palavra 
    for i in palavra:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            x = x.replace(i,'')
    return x