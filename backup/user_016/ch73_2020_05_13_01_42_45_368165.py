def remove_vogais(x):
    for i in x:
        if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
            x = x.replace(i,'')
    return x
        