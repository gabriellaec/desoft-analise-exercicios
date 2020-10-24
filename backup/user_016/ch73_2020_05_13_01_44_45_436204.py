def remove_vogais(x):
    for i in x:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            x = x.replace(i,'')
    return x
        