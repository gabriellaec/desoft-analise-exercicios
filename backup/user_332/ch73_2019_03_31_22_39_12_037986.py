def remove_vogais (palavra):
    for e in palavra:
        if (e == 'a' or e == 'e' or e == 'i' or e == 'o' or e == 'u'):
            palavra.replace(e ,'')
            
    return palavra
