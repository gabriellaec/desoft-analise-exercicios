def remove_vogais(texto):
    string=''
    i=0
    while i in texto:
        if i!='a' and i!='e' and i!='i' and i!='o' and i!='u':
            string+=i
    return string