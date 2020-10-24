def remove_vogais(texto):
    pa=''
    for i in texto:
        if i!='a' and i!='e' and i!='i' and i!='o' and i!='u':
            pa+=texto[i]
    return pa