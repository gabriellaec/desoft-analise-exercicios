def remove_vogais(texto):
    string=''
    i=0
    while i<len(texto):
        if i!='a' and i!='e' and i!='i' and i!='o' and i!='u':
            string+=texto[i]
    return string